# replace excape column names with empty space with underscore "_"
excape.columns = excape.columns.str.replace(' ','_')

# print the dimensions of excape dataframe
print(excape.shape)

excape.Activity_Flag.unique()

#  log10 of concentration value in MOLAR units
#  np.log10(1.81e-9)

#other useful info:
#- standard relation column
#- assay information

# important: need to verify that all the assays are measuring the same thing
len(chembl.Assay_Description.unique())
