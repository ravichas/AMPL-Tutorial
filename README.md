![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/ATOM.PNG)

The ATOM Modeling PipeLine (AMPL; https://github.com/ATOMconsortium/AMPL) is an open-source, modular, extensible software pipeline for building and sharing models to advance in silico drug discovery.

This repository contains a collection of experimental AMPL-COLAB tutorial notebooks.  

### Basic Google COLAB Introduction
* [Tutorial-00:](https://github.com/ravichas/AMPL-Tutorial/blob/master/BasicCOLAB_Tutorial.ipynb) Basic COLAB tutorial

### Data Collection and creating Machine-Learning ready datasets:

#### Data ingestion, mergin, curation and featurization

#### Explore HTR3A binding data from ExCAPE-DB
* [Tutorial-01:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_excape_min_viable_one.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for data curation, EDA and clustering on ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) data for HTR3A protein (modified from Dr. Jonathan Allen's notebook)

* [Tutorial-02:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_excape_2_curation.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for Data curation of HTR3A protein data from ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) Data (modified from Dr. Jonathan Allen's notebook)

#### Explore HTR3A binding data from Drug Target Commons database

* [Tutorial-03:](https://github.com/ravichas/AMPL-Tutorial/blob/master/explore_data_dtc_min_viable_one.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for Data curation of HTR3A protein data from DTC (https://solr.ideaconsult.net/search/excape/) Data (modified from Dr. Jonathan Allen's notebook)

#### Explore HTR3A binding data from ChEMBL database
* [Tutorial-04:](https://github.com/ravichas/AMPL-Tutorial/blob/master/EDA_Curate_Merge_Visualize.ipynb) (**Mode: AMPL_GPU; Time: ~ 4 minutes**)
This COLAB notebook will use AMPL to upload datasets (small-molecule activity data from ChEMBL), clean, merge and do some basic Exploratory Data Analysis.  



### Model training and tuning:

* [Tutorial-05:](https://github.com/ravichas/AMPL-Tutorial/blob/master/Delaney_Example.ipynb) (**Time: ~ 2 minutes**): Simple supervised learning example.
AMPL will read the public data (117 chemical compounds), curate, fit a RandomForest model to predict solubility and test the model. For additional information on the dataset, please check this publication,https://pubmed.ncbi.nlm.nih.gov/15154768/ 
![Delaney](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/Delaney.PNG | width=250)

* [Tutorial-06:](https://github.com/ravichas/AMPL-Tutorial/blob/master/Delaney_Example_AMPL_GPU.ipynb) (**Mode: AMPL_GPU; Time: ~ 2 minutes**): 
This AMBL-COLAB notebook uses example Tutorial-01 except AMPL in GPU mode (AMPL_GPU)

* [Tutorial-07:](https://github.com/ravichas/AMPL-Tutorial/blob/master/CHEMBL26_SCN5A_IC50_example.ipynb) (**Mode: AMPL_GPU; Time: ~ 18 minutes**): 
This COLAB notebook will use AMPL for predicting binding affinities -pIC50 values- of ligands that could bind to human **Sodium channel protein type 5 subunit alpha** protein (Gene: SCN5A) using Graph Convolutional Network Model. ChEMBL database is the data source of binding affinities (pIC50)
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/SCN5A.PNG)

### Creating and using metrics for analyzing model performance: (coming soon)

### Hyper-parameter Optimization (coming soon)

### Creating high-quality models (coming soon)

### Exploring AMPL functions for saving models and loading prebuild models for prediction (coming soon)

### Model Inference: 
This notebook loads a model from a published work, https://arxiv.org/abs/2002.12541, and makes an inference with an example dataset, 
https://github.com/ravichas/AMPL-Tutorial/blob/master/BSEP_modeling.ipynb) 

#### Similar chemoinformatics, drug-discovery software tools:
* DeepChem, https://deepchem.io/
* rdkit, https://www.rdkit.org/

## Acknowledgements: 
* Amanda Paulson
* Ben Madej 
* Da Shi
* Hiran Ranganathan
* Jonathan Allen
* Kevin Mcloughlin
* Ya Ju Fan

