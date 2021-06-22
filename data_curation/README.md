# Scope of the ATOM Modeling Pipeline (AMPL) script

To automate the data download from public target binding data from chemoinformatics databases such as ChEMBL, Drug Target Commons (DTC), ExCAPE-DB etc and create 
machine-learning ready datasets (combined and individuval) along with some simple Exploratory Data Analysis plots. Users with some effort can add -need Python programming- other input databas sources by extending the code.   

### Requirements: 

AMPL installation. Plese check AMPL GitHub page for installation, https://github.com/ATOMconsortium/AMPL 

## File structure details of the sourceCuration tar file

Python code: custom_config.py, custom_data_curation.py, target_data_curation.py
Main driver input and configuration files: example.sh, priority_panel_ki.ini
Data input: tar_gene_chembl.txt, tar_gene.txt, gene_lst_v1.txt 
Output folders: tempDataKi, tempPlotKi 

Here is a tree structure of the tar file:
```
sourceCuration
├── custom_config.py
├── custom_data_curation.py
├── target_data_curation.py
├── example.out  (output)
├── example.sh   (main script)
├── gene_lst_v1.txt (list of DTC formatted genes)
├── priority_panel_ki.ini (configuration file)
├── tar_gene_chembl.txt  (list of chembl genes)
├── tar_gene.txt (list of excape formatted genes)
├── tempDataKi
│   └── This-is-a-Folder-for-output-data
└── tempPlotKi
    └── This-is-a-Folder-for-output-plots-in-pdf
    
MultipleSourceCurn
├── [4.0K]  DB
│   ├── [2.1G]  DTC_data.csv          # Drug Data Commons (DTC) data 
│   ├── [ 95M]  inchikey_smiles.csv   # DTC InChi to SMILES mapping list
│   ├── [ 18G]  pubchem.chembl.dataset4publication_inchi_smiles.tsv  # Excape-DB
│   ├── [2.1G]  uid2cact.json         # ChEMBL DB
│   └── [557K]  uid2gn_human.json     # ChEMBL DB
└── [4.0K]  sourceCuration
    ├── [ 555]  custom_config.py
    ├── [ 16K]  custom_data_curation.py
    ├── [1.1K]  debug.ipynb
    ├── [ 647]  example.sh (driver script)
    ├── [  24]  gene_lst_v1.txt       # input gene list for ExCAPE-DB extraction
    ├── [2.3K]  priority_panel_ki.ini # Configuration file that contains all the other DB file path
    ├── [  24]  tar_gene.txt          # input gene list
    ├── [  36]  tar_gene_chembl.txt   # input gene list for ChEMBL DB extraction)
    ├── [  24]  tar_list.txt          # input gene list for DTC DB extraction)
    ├── [ 20K]  target_data_curation.py
    ├── [4.0K]  tempDataKi
    │   └── # This-is-a-Folder-for-output-data
    └── [4.0K]  tempPlotKi
        └── # This-is-a-Folder-for-output-plots-in-pdf
```

DB directory details: 

Due to large DB directory size (~ 22 GB), its contents are not included in the MultipleSourceCurn.tar.gz file. 
After downloading MultipleSourceCurn.tar.gz, use `tar -xzvf MutipleSourceCurn.tar.gz`, to untar/unzip the 
file. This will create `MultipleSourceCurn` folder. Please download the concerned files and place them under the 
DB folder. Make sure the filenames match the filenames listed under `Data


output_data_dir (str) : directory location to put combined model ready dataset and rejected compounds.
output_img_dir (str) : location to put diagnostic data , currently just distribution of activity values for final set"
comb (dictionary) : dictionary with key as gene target and value as CustomActivityDump class
comb_type (str): pre_curated (default) combines the datasets from different sources that were individually curated. 
Not yet implemented is a raw option to re-combine all data

Test run: 
Python code was tested for single and multiple protein targets along with different choices 
for the accumulation assay data type (ki, IC50 etc.)  

Here are some details on computational time for a test set of 3 protein targets, CASP9, KCNH2 and CYP3A4 with 
three end_points (ChEMBL definition;  ) IC50, Ki and EC50 and three data sources, DTC, ExcapeDB and ChEMBL. 

System tested: Google Cloud Platform (GCP), Intel Haswell CPU with 4vCPUs and 100GB memory. 
Peak memory usuage was ~80 GB. Here is the time to extract and curate data.

real    51m49.211s
user    50m9.502s
sys     0m59.148s

## Data files 

Please note that the data files 

## Excape

Visit Excape download site, https://zenodo.org/record/2543724#.YMtnGahKguU,
and download the latest dataset. The file will be xz format compressed file. 
To uncompress, use the following command: 
(At the time of download, v2 was available; please check the downloaded file and replace the 
filename accordingly)
xz -d pubchem.chembl.dataset4publication_inchi_smiles_v2.tsv.xz 

Warning: the file could take upto ~20 GB. 
# here is how you can extract a single target (ex. HTR3A) related data.
```
awk -F'\t' '$9 == "HTR3A"'  pubchem.chembl.dataset4publication_inchi_smiles.tsv > temp
```
## DTC

Visit http://drgutargetcommons.fimm.fi/ 

```
DB
├── [4.0K]  ChEMBL
│   └── [4.0K]  raw
│       ├── [1.1G]  uid2cact.json
│       └── [557K]  uid2gn_human.json
├── [4.0K]  DTC
│   ├── [2.1G]  DTC_data.csv
│   └── [4.0K]  raw
│       └── [4.0K]  pubchem_smiles
│           └── [ 95M]  inchikey_smiles.csv
└── [4.0K]  excapedb
    └── [ 18G]  pubchem.chembl.dataset4publication_inchi_smiles.tsv
```


