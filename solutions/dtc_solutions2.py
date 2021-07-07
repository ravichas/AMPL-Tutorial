dtc=dtc.replace('None', np.nan)
dtc.head()

dtc.standard_units.unique() #already all nM

dtc.standard_type.unique()

dtc[dtc.standard_units=='NM'].standard_type.unique()

## **Curation step:** create pValues from normal values

# add pX column
dtc['pDTC_Value'] = np.where(dtc.standard_units == 'NM',
                             -np.log10(dtc.standard_value/1000000000 ),
                             dtc.standard_value)

dtc.describe()

numeric_cols=['standard_value', 'pDTC_Value']
dtc[numeric_cols].hist(bins=20, figsize=(10,5));

dtc_types=dtc.pivot_table(index = 'compound_id', columns = 'standard_type', values='standard_value', aggfunc='mean')
display(dtc_types.describe())
dtc_types.hist(figsize=(13,13));

dtc_types=dtc.pivot_table(index = 'compound_id', columns = 'standard_type', values='pDTC_Value', aggfunc='mean')
display(dtc_types.describe())
dtc_types.hist(figsize=(10,10));
