![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/ATOM.PNG)

The ATOM Modeling PipeLine (AMPL; https://github.com/ATOMconsortium/AMPL) is an open-source, modular, extensible software pipeline for building and sharing models to advance in silico drug discovery. To see the list of AMPL parameters, please check this link,  https://github.com/ATOMconsortium/AMPL/blob/master/atomsci/ddm/docs/PARAMETERS.md

This repository contains a collection of experimental AMPL-COLAB tutorial notebooks.  

## 0. Basic Google COLAB Introduction (Works best with Google Chrome)
* [Tutorial-00:](https://github.com/ravichas/AMPL-Tutorial/blob/master/BasicCOLAB_Tutorial.ipynb) Basic COLAB tutorial. For all the COLAB tutorials, click on the tutorial link, and then click on "Open in Colab" baner. You can open and run the notebook from the browser. If you want to save your edits to the notebook, you need to save a copy in your Google Drive. Usually, Google COLAB saves the notebook files under the "My Drive > Colab Notebooks" folder

## 1. Data Collection and creating Machine-Learning ready datasets:

The data that we collect for modeling is small-molecule/drug binding data. The following links will introduce some of the concepts and outcome measures related to this topic:
* https://en.wikipedia.org/wiki/IC50
* https://bpspubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1476-5381.2009.00604.x

For the tutorials, we will use the small-molecule data obtained from ChEMBL, Drug Target Commons (DTC) and Excape-DB. Look at the end of this document for the database links. 

* ChEMBL & Escape-DB: For a single target data, it is easy to download from the DB websites
* Drug Target Commons (DTC): Please see below

<b> DTC: </b>
* Some of the DTC target related information (ex Target: CYP3A4) will be big (> 46K compounds and ~ 16 MB) and sometimes will take a long time to export them into Excel file. The best option would be to download the whole DTC dataset (~ 2 GB) and extract the target of your interest from the master file. Here are the steps:
    *   Visit DTC site, https://drugtargetcommons.fimm.fi/ 
    *   Download the whole dataset (I am assuming that you are using a Linux or Mac OS for this exercise)
    *   Extract the target of your interest (e.g., CYP3A4) using the following Linux shell commands:

            ```
            wget https://drugtargetcommons.fimm.fi/static/Excell_files/DTC_data.csv -o DTC_data.csv 
            grep CYP3A4 DTC_data.csv > raw_data.txt 
            head -1 DTC_data.csv > header 
            cat header raw_data.txt > DTC_CYP3A4.csv 
            ```

### Data ingestion, merging, curation and featurization

Here are the key steps of AMPL data curation (reading binding data (ex. DTC), extracting SMILES from PubChem, creating standardized SMILES, merging multiple assay values after dealing with high variant values; for details, look at the tutorial notebooks from this section):
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/AMPL_data_curation_steps.png)


### Explore HTR3A binding data from ExCAPE-DB
* [Tutorial-01:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_excape_min_viable_one.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for data cleaning, EDA and clustering on ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) data for HTR3A protein 

* [Tutorial-02:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_excape_2_curation.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for data curation of HTR3A protein data from ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) Data 

### Explore HTR3A binding data from Drug Target Commons database

* [Tutorial-03:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_dtc_min_viable_one.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for Data cleaning, EDA and clustering of HTR3A protein data from Drug Target Commons (DTC)  
* [Tutorial-04:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_dtc_2_curate.ipynb) (**Mode: AMPL_GPU; Time: ~ 10 minutes**)
This COLAB notebook will use AMPL for Data curation of HTR3A protein data from Drug Target Commons (DTC)

### Curating, merging and visualizing two datasets 
* [Tutorial-05:](https://github.com/ravichas/AMPL-Tutorial/blob/master/EDA_Curate_Merge_Visualize.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL to upload datasets (small-molecule activity data from ChEMBL), clean, merge and do some basic Exploratory Data Analysis. 
* [Tutorial-06:](https://github.com/ravichas/AMPL-Tutorial/blob/master/combine_data_step_4.ipynb) (**Mode: AMPL_GPU**)
This COLAB notebook with use AMPL to merge HTR3A binding data from two different data sources, DTC and ExCAPE-DB.

### EDA Notebooks
* [Tutorial-07:](https://github.com/ravichas/AMPL-Tutorial/blob/master/EDA_With_Harmonization.ipynb) The notebook uses HTR3A as the protein target. The notebook accomplishes the following tasks:
   * Uses AMPL software
   * Reads in data from three database sources: ChEMBL, Excape-DB and DTC 
   * Cleans, standardizes and analyzes the data
   * Merges and harmonizes to create a dataset
* [Tutorial-07a:](https://github.com/ravichas/AMPL-Tutorial/blob/master/EDA_noAMPL_InstructorCopy.ipynb) Instructor completed template notebook for the target HTR3A. This notebook is different from Tutorial-07 in the following way:
   *  Uses standalone libraries 
   *  Repeats all the above mentioned steps of Tutorial-07

## 2. Model training and tuning:

### Random Forest modeling to predict solubility (GPU)
* [Tutorial-08:](https://github.com/ravichas/AMPL-Tutorial/blob/master/Delaney_Example.ipynb) (**Time: ~ 2 minutes**): Simple supervised learning example.
AMPL will read the public data (117 chemical compounds), curate, fit a Random Forest model to predict solubility and test the model. For additional information on the dataset, please check this publication,https://pubmed.ncbi.nlm.nih.gov/15154768/
![Delaney](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/Delaney.PNG)

### Graph Convolution modeling to predict SCN5A binding affinities (GPU)
* [Tutorial-09:](https://github.com/ravichas/AMPL-Tutorial/blob/master/CHEMBL26_SCN5A_IC50_example.ipynb) (**Mode: AMPL_GPU; Time: ~ 18 minutes**): 
This COLAB notebook will use AMPL for predicting binding affinities -pIC50 values- of ligands that could bind to human **Sodium channel protein type 5 subunit alpha** protein (Gene: SCN5A) using Graph Convolutional Network Model. ChEMBL database is the data source of binding affinities (pIC50)
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/SCN5A.PNG)

## 3. Hyper-parameter Optimization (HPO), Uncertainty Quantification (UQ), and using metrics for analyzing model performance. 

This notebook also explores AMPL functions for saving and loading prebuild AMPL models for analysis. 
* [Tutorial-10](https://github.com/ravichas/AMPL-Tutorial/blob/master/AMPL_HPO_demo.ipynb) Hyper-parameter Optimization [(HPO)](https://en.wikipedia.org/wiki/Hyperparameter_optimization) and Uncertainty Quantification [(UQ)](https://en.wikipedia.org/wiki/Uncertainty_quantification).
* [Tutorial-11](https://github.com/ravichas/AMPL-Tutorial/blob/master/AMPL_HPO_Part2.ipynb) Notebook includes HPO Grid Search on three different modeling methods (Random Forest, NN and XGBoost).

## 4. Creating high-quality models 
* [Tutorial-12](https://github.com/ravichas/AMPL-Tutorial/blob/master/AMPL_EDA_Part2.ipynb) Notebook provides the framework for visualizing the resutls of HPO results and use them to identify best models. 

### 5. Model Inference: 
* [Tutorial-13:] (https://github.com/ravichas/AMPL-Tutorial/blob/master/BSEP_modeling.ipynb) This notebook creates an AMPL (RF) model using BSEP dataset (reference: https://arxiv.org/abs/2002.12541), and makes predictions (inference) on an external sample test dataset.   
 

## Supporting links

### Similar chemoinformatics, drug-discovery software tools:
* DeepChem, https://deepchem.io/
* rdkit, https://www.rdkit.org/

### Chemoinformatics databases
* ChEMBL: https://www.ebi.ac.uk/chembl/
* PubChem: https://pubchem.ncbi.nlm.nih.gov/
* Drug Target Commons (DTC): https://drugtargetcommons.fimm.fi/
* ExCAPE-DB: https://solr.ideaconsult.net/search/excape/
* DrugBank: https://go.drugbank.com/

## Acknowledgements
Most of the tutorial code chunks came from multple Jupyter notebooks generously shared by the ATOM team. 
* Amanda Paulson
* Ben Madej 
* Da Shi
* Hiran Ranganathan
* Jonathan Allen
* Kevin Mcloughlin
* Ya Ju Fan

