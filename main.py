import pandas as pd
df = pd.read_csv(r'C:\Users\bahez\OneDrive\Desktop\pyWithBara\organizations-100.csv',header=None,names=['orga','late'],usecols=[0,4],na_values=['?'],nrows=25,skiprows=25)
df.isna().sum()
df.dropna(inplace=True)
print(df)
help(pd.read_csv)