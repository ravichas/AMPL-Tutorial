![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/ATOM.PNG)

<h2> The ATOM Modeling PipeLine (AMPL; https://github.com/ATOMconsortium/AMPL) is an open-source, modular, extensible software pipeline for building and sharing models to advance in silico drug discovery.

This repository contains a collection of experimental AMPL tutorial COLAB notebooks.  

<style>Test{color:red;}</style>

* **Tutorial-00:** https://github.com/ravichas/AMPL-Tutorial/blob/master/00_BasicCOLAB_Tutorial.ipynb : Basic COLAB tutorial

* **Tutorial-01:** https://github.com/ravichas/AMPL-Tutorial/blob/master/01_Delaney_Example.ipynb (**Time: ~ 2 minutes**): 
![Delaney](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/Delaney.PNG)
For background information, please check this publication,https://pubmed.ncbi.nlm.nih.gov/15154768/
This AMBL-COLAB notebook will take a public dataset of about 117 compounds with chemical properties and smiles strings. AMPL will read the data, curate, fit a RandomForest model to predict solubility and test the model. 

* **Tutorial-02:** https://github.com/ravichas/AMPL-Tutorial/blob/master/02_Delaney_Example_AMPL_GPU.ipynb (**Mode: AMPL_GPU; Time: ~ 2 minutes**): This AMBL-COLAB notebook will take a public dataset of about 117 compounds with chemical properties and smiles strings. AMPL_GPU will read the data, curate, fit a RandomForest model to predict solubility and test the model. 

* **Tutorial-03:** https://github.com/ravichas/AMPL-Tutorial/blob/master/03_CHEMBL26_SCN5A_IC50_example.ipynb (**Mode: AMPL_GPU; Time: ~ 18 minutes**): 
![Test Image 1](https://github.com/ravichas/AMPL-Tutorial/blob/master/Img/SCN5A.PNG)
This AMPL-COLAB notebook will use AMPL for predicting binding affinities -pIC50 values- of ligands that could bind to human **Sodium channel protein type 5 subunit alpha** protein (Gene: SCN5A) using Graph Convolutional Network Model. ChEMBL database is the source of the binding affinities (pIC50)


