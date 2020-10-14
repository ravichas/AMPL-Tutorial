![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/ATOM.PNG)

The ATOM Modeling PipeLine (AMPL; https://github.com/ATOMconsortium/AMPL) is an open-source, modular, extensible software pipeline for building and sharing models to advance in silico drug discovery.

This repository contains a collection of experimental AMPL-COLAB tutorial notebooks.  

* **Tutorial-00:** https://github.com/ravichas/AMPL-Tutorial/blob/master/00_BasicCOLAB_Tutorial.ipynb : Basic COLAB tutorial


* **Tutorial-01:** https://github.com/ravichas/AMPL-Tutorial/blob/master/01_Delaney_Example.ipynb (**Time: ~ 2 minutes**): Simple supervised learning example.
AMPL will read the public data (117 chemical compounds), curate, fit a RandomForest model to predict solubility and test the model. For additional information on the dataset, please check this publication,https://pubmed.ncbi.nlm.nih.gov/15154768/ 
![Delaney](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/Delaney.PNG)


* **Tutorial-02:** https://github.com/ravichas/AMPL-Tutorial/blob/master/02_Delaney_Example_AMPL_GPU.ipynb (**Mode: AMPL_GPU; Time: ~ 2 minutes**): 
This AMBL-COLAB notebook uses example Tutorial-01 except AMPL in GPU mode (AMPL_GPU)

* **Tutorial-03:** https://github.com/ravichas/AMPL-Tutorial/blob/master/03_CHEMBL26_SCN5A_IC50_example.ipynb (**Mode: AMPL_GPU; Time: ~ 18 minutes**): 
This COLAB notebook will use AMPL for predicting binding affinities -pIC50 values- of ligands that could bind to human **Sodium channel protein type 5 subunit alpha** protein (Gene: SCN5A) using Graph Convolutional Network Model. ChEMBL database is the data source of binding affinities (pIC50)
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/SCN5A.PNG)


