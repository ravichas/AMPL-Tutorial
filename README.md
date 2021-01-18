![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/ATOM.PNG)

The ATOM Modeling PipeLine (AMPL; https://github.com/ATOMconsortium/AMPL) is an open-source, modular, extensible software pipeline for building and sharing models to advance in silico drug discovery.

Similar chemoinformatics, drug-discovery software tools:
* DeepChem, https://deepchem.io/
* rdkit, https://www.rdkit.org/

This repository contains a collection of experimental AMPL-COLAB tutorial notebooks.  

* **Tutorial-00:** https://github.com/ravichas/AMPL-Tutorial/blob/master/00_BasicCOLAB_Tutorial.ipynb : Basic COLAB tutorial

* **[Tutorial-01:]**(https://github.com/ravichas/AMPL-Tutorial/blob/master/01_Delaney_Example.ipynb) (**Time: ~ 2 minutes**): Simple supervised learning example.
AMPL will read the public data (117 chemical compounds), curate, fit a RandomForest model to predict solubility and test the model. For additional information on the dataset, please check this publication,https://pubmed.ncbi.nlm.nih.gov/15154768/ 
![Delaney](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/Delaney.PNG)

* **Tutorial-02:** https://github.com/ravichas/AMPL-Tutorial/blob/master/02_Delaney_Example_AMPL_GPU.ipynb (**Mode: AMPL_GPU; Time: ~ 2 minutes**): 
This AMBL-COLAB notebook uses example Tutorial-01 except AMPL in GPU mode (AMPL_GPU)

* **Tutorial-03:** https://github.com/ravichas/AMPL-Tutorial/blob/master/03_CHEMBL26_SCN5A_IC50_example.ipynb (**Mode: AMPL_GPU; Time: ~ 18 minutes**): 
This COLAB notebook will use AMPL for predicting binding affinities -pIC50 values- of ligands that could bind to human **Sodium channel protein type 5 subunit alpha** protein (Gene: SCN5A) using Graph Convolutional Network Model. ChEMBL database is the data source of binding affinities (pIC50)
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/SCN5A.PNG)

* **Tutorial-04:** https://github.com/ravichas/AMPL-Tutorial/blob/master/04_EDA_Curate_Merge_Visualize.ipynb (**Time: ~ 4 minutes**)
This COLAB notebook will use AMPL to upload datasets (small-molecule activity data from ChEMBL), clean, merge and do some basic Exploratory Data Analysis.  

* **Tutorial-05:** https://github.com/ravichas/AMPL-Tutorial/blob/master/05_explore_data_excape_2_curation.ipynb (**Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for Data curation of HTR3A protein data from ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) Data (modified from Dr. Jonathan Allen's notebook)

* **Tutorial-06:** https://github.com/ravichas/AMPL-Tutorial/blob/master/06_explore_data_excape_min_viable_one.ipyn (**Time: ~ 4 minutes**)
This COLAB notebook will use AMPL for data curation, EDA and clustering on ExCAPE-DB (https://solr.ideaconsult.net/search/excape/) data for HTR3A protein (modified from Dr. Jonathan Allen's notebook)



