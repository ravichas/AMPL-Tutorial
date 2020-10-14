# Code to compute distances between top ideated compounds from an Aurk pilot run and the nearest
# neighbor compounds in the combined GSK AurkA/AurkB assay dataset

import os
import sys
from atomsci.ddm.pipeline import chem_diversity as cd
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from atomsci.ddm.utils.struct_utils import base_smiles_from_smiles
from scipy.spatial.distance import squareform, cdist, pdist
import umap

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.style.use('ggplot')
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)
matplotlib.rc('axes', labelsize=12)



def compute_dist_matrix(pred_file, ref_dset_file, pred_smiles_col='smiles', ref_smiles_col='base_rdkit_smiles'):
    """
    Compute the Tanimoto distance matrix between the SMILES strings in pred_file and those in ref_dset_file.
    """
    base = os.path.splitext(os.path.basename(pred_file))

    pred_df = pd.read_csv(pred_file, index_col=False)
    ref_df = pd.read_csv(ref_dset_file, index_col=False)
    pred_smiles = pred_df[pred_smiles_col].values
    pred_smiles = [base_smiles_from_smiles(s) for s in pred_smiles]
    ref_smiles = ref_df[ref_smiles_col].values

    dist_arr = cd.calc_dist_smiles('ecfp', 'tanimoto', pred_smiles, ref_smiles, calc_type='all')
    return dist_arr


def nearest_neighbor_distances(pred_dset, ref_dset, pred_smiles_col='smiles', ref_smiles_col='base_rdkit_smiles'):
    """
    Find the nearest neighbor compound in the reference dataset for each predicted compound and its distance to
    the predicted compound. Add this information to the table of predicted properties.
    """

    if type(pred_dset) == str:
        pred_df = pd.read_csv(pred_dset, index_col=False)
    else:
        pred_df = pred_dset
    if type(ref_dset) == str:
        ref_df = pd.read_csv(ref_dset, index_col=False)
    else:
        ref_df = ref_dset
    pred_smiles = pred_df[pred_smiles_col].values
    pred_smiles = [base_smiles_from_smiles(s) for s in pred_smiles]
    ref_smiles = ref_df[ref_smiles_col].values

    dist_arr = cd.calc_dist_smiles('ecfp', 'tanimoto', pred_smiles, ref_smiles, calc_type='all')
    ref_cmpd_ids = ref_df.compound_id.values

    nn_ind = np.argmin(dist_arr, axis=1)
    nn_dist = np.min(dist_arr, axis=1)
    pred_df['nearest_cmpd'] = ref_cmpd_ids[nn_ind]
    pred_df['nearest_dist'] = nn_dist
    uniq_neighbors, counts = np.unique(pred_df.nearest_cmpd.values, return_counts=True)
    nnfreq_df = pd.DataFrame(dict(nearest_cmpd=uniq_neighbors, pred_cmpd_count=counts)).sort_values(
                                                               by='pred_cmpd_count', ascending=False)
    nn_pred_df = pred_df.merge(nnfreq_df, how='left', on='nearest_cmpd').sort_values(
                                                               by=['pred_cmpd_count', 'nearest_cmpd'], ascending=False)
    return nn_pred_df

def mcs_vs_tanimoto(pred_dset, pred_smiles_col='smiles'):
    """
    Compute within-dataset distance matrices for compounds in pred_dset based on both Tanimoto and MCS
    distances, and compare the resulting distances.

    """
    if type(pred_dset) == str:
        pred_df = pd.read_csv(pred_dset, index_col=False)
    else:
        pred_df = pred_dset
    pred_smiles = pred_df[pred_smiles_col].values
    pred_smiles = [base_smiles_from_smiles(s) for s in pred_smiles]
    cmpd_ids = pred_df.compound_id.values
    ncmpd = pred_df.shape[0]

    cmpd_i_list = []
    cmpd_j_list = []
    tani_dist = []
    mcs_dist = []

    tani_dist_mat = cd.calc_dist_smiles('ecfp', 'tanimoto', pred_smiles, calc_type='all')
    mcs_dist_mat = cd.calc_dist_smiles('ecfp', 'mcs', pred_smiles, calc_type='all')
    for i in range(ncmpd-1):
        cmpd_i = cmpd_ids[i]
        for j in range(i+1, ncmpd):
            cmpd_j = cmpd_ids[j]
            cmpd_i_list.append(cmpd_i)
            cmpd_j_list.append(cmpd_j)
            tani_dist.append(tani_dist_mat[i,j])
            mcs_dist.append(mcs_dist_mat[i,j])

    dist_df = pd.DataFrame(dict(
                compound_i = cmpd_i_list,
                compound_j = cmpd_j_list,
                tanimoto_distance = tani_dist,
                mcs_distance = mcs_dist ))
    fig, ax = plt.subplots(figsize=(15,15))
    sns.scatterplot(x='mcs_distance', y='tanimoto_distance', data=dist_df)

    return dist_df

def umap_fps(pred_dset, ref_dset, pred_smiles_col='smiles', ref_smiles_col='base_rdkit_smiles', label_col = 'compound_id', commonest_nn_id='GSK2189002A'):
    """
    Fit a 2D UMAP projector to the fingerprints of the reference dataset compounds. Plot the projected
    fingerprints for these compounds, and overlay the plot with the projected fingerprints of the
    predicted compounds.
    """

    """
    AKP: refactor to allow for 'none' type pred_dset in order to just UMAP a single dataset.
    Also remove references to dir's since they're not needed / break function
    """

    if type(ref_dset) == str:
        ref_df = pd.read_csv(ref_dset, index_col=False)
    else:
        ref_df = ref_dset

    ref_smiles = ref_df[ref_smiles_col].values

    #data_dir = os.path.dirname(pred_file)
    #pred_basename = os.path.splitext(os.path.basename(pred_file))[0]
    #nn_pred_file = '%s/%s_nearest_ref_cmpd_tanimoto.csv' % (data_dir, pred_basename)
    #pred_df = pd.read_csv(nn_pred_file, index_col=False)
    
    
    ref_mols = [Chem.MolFromSmiles(smiles) for smiles in ref_smiles if str(smiles) != 'nan']
    ref_nmissing = sum([mol is None for mol in ref_mols])
    if ref_nmissing > 0:
        print("RDKit couldn't read %d reference smiles strings" % ref_nmissing)
        ref_mols = [mol for mol in ref_mols if mol is not None]
    
    ref_fps = [AllChem.GetMorganFingerprintAsBitVect(mol, 2, 1024) for mol in ref_mols]
    ref_fpdata = np.array(ref_fps, dtype=int)

    mapper = umap.UMAP(n_neighbors=10, n_components=2, metric='jaccard')
    mapper.fit(ref_fpdata)
    ref_reps = mapper.transform(ref_fpdata)
    ref_rep_df = pd.DataFrame.from_records(ref_reps, columns=['umap_X', 'umap_Y'])

    nref = ref_rep_df.shape[0]
    ref_sources = np.array([' Reference set'] * nref)

    if pred_dset is not None:
        if type(pred_dset) == str:
            pred_df = pd.read_csv(pred_dset, index_col=False)
        else:
            pred_df = pred_dset

        pred_smiles = pred_df[pred_smiles_col].values
        pred_mols = [Chem.MolFromSmiles(smiles) for smiles in pred_smiles if str(smiles) != 'nan']
        pred_nmissing = sum([mol is None for mol in pred_mols])
        if pred_nmissing > 0:
            print("RDKit couldn't read %d predicted smiles strings" % pred_nmissing)
            pred_mols = [mol for mol in pred_mols if mol is not None]

        pred_fps = [AllChem.GetMorganFingerprintAsBitVect(mol, 2, 1024) for mol in pred_mols]
        pred_fpdata = np.array(pred_fps, dtype=int)
        pred_reps = mapper.transform(pred_fpdata)
        pred_rep_df = pd.DataFrame.from_records(pred_reps, columns=['umap_X', 'umap_Y'])

        for i, smiles in enumerate(ref_smiles):
            if smiles in pred_smiles:
                ref_sources[i] = 'Rediscovered'

    ref_sources[ref_df.compound_id.values == commonest_nn_id] = 'commonest NN'
    ref_rep_df['compound_type'] = ref_sources
    ref_rep_df['compound_id'] = ref_df.compound_id.values
    ref_rep_df['label'] = ref_df[label_col].values

    
    #rep_df = pd.DataFrame()

    if pred_dset is not None:
        pred_rep_df['compound_type'] = 'Generated'
        #pred_rep_df['compound_id'] = ''
        pred_rep_df['compound_id'] = pred_df.compound_id.values
        pred_rep_df['label'] = pred_df[label_col].values
        rep_df = pd.concat((ref_rep_df, pred_rep_df), ignore_index=True)
    else:
        rep_df = ref_rep_df

    return rep_df

def mcs_vs_tanimoto_nn_dist(dist_df, pred_df):
    """
    For each compound with MCS and Tanimoto distances to other compounds in dist_df, find the nearest
    neighbors by MCS distances and by Tanimoto distance. Plot the MCS distance to the nearest Tanimoto neighbor
    against the MCS distance to the nearest MCS neighbor. Ditto with Tanimoto distances.
    """
    cmpd_ids = pred_df.compound_id.values
    ncmpd = pred_df.shape[0]
    mcs_dist_mat = squareform(dist_df.mcs_distance.values)
    tani_dist_mat = squareform(dist_df.tanimoto_distance.values)

    # Get nearest neighbor that isn't the compound itself
    mcs_ind = np.argsort(mcs_dist_mat, axis=1)
    mcs_nn_ind = mcs_ind[:,1]
    mcs_nn_dist = mcs_dist_mat[range(ncmpd), mcs_nn_ind]

    pred_df['mcs_nn_cmpd'] = cmpd_ids[mcs_nn_ind]
    pred_df['mcs_dist_mcs_nn'] = mcs_nn_dist

    tani_ind = np.argsort(tani_dist_mat, axis=1)
    tani_nn_ind = tani_ind[:,1]
    tani_nn_dist = tani_dist_mat[range(ncmpd), tani_nn_ind]

    pred_df['tani_nn_cmpd'] = cmpd_ids[tani_nn_ind]
    pred_df['tani_dist_tani_nn'] = tani_nn_dist

    pred_df['mcs_dist_tani_nn'] = mcs_dist_mat[range(ncmpd), tani_nn_ind]
    pred_df['tani_dist_mcs_nn'] = tani_dist_mat[range(ncmpd), mcs_nn_ind]

    fig, ax = plt.subplots(figsize=(12,12))
    sns.scatterplot(x='mcs_dist_mcs_nn', y='mcs_dist_tani_nn', data=pred_df)

    fig, ax = plt.subplots(figsize=(12,12))
    sns.scatterplot(x='tani_dist_tani_nn', y='tani_dist_mcs_nn', data=pred_df)

    return pred_df