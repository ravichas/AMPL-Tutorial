excape=excape.replace('None', np.nan)
excape.head()

# excape only has one column we care about
display(excape.describe())
excape.pXC50.hist(figsize=(5,5));
