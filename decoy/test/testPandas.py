import pandas as pd

country=pd.read_csv('country_names.tsv',sep='\t',header=0)
print(country.head(10))
