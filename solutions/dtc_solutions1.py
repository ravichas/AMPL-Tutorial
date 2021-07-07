dtc.columns = dtc.columns.str.replace(' ','_')
print("dtc.shape: ", dtc.shape)
temp = pd.DataFrame(dtc['standard_type'].value_counts()).T
print(temp)

dtc = dtc[dtc.standard_type.isin(['KI', 'Ki', 'IC50', 'EC50'])]

# change KI to Ki
dtc.standard_type = np.where(dtc.standard_type == 'KI', 'Ki', dtc.standard_type)
dtc.standard_type.unique()

dtc.head(3)
