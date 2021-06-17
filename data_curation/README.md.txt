## Excape

Visit Excape download site, https://zenodo.org/record/2543724#.YMtnGahKguU,
and download the latest dataset. The file will be xz format compressed file. 
To uncompress, use the following command: 
(At the time of download, v2 was available; please check the downloaded file and replace the 
filename accordingly)
xz -d pubchem.chembl.dataset4publication_inchi_smiles_v2.tsv.xz 

Warning: the file could take upto ~20 GB. 
# here is how you can extract a single target (ex. HTR3A) related data.
awk -F'\t' '$9 == "HTR3A"'  pubchem.chembl.dataset4publication_inchi_smiles.tsv > temp

## DTC

Visit http://drgutargetcommons.fimm.fi/ 

