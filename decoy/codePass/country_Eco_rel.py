import pandas as pd
import json
def valueof(a,b):
    return int(b)-int(a)/100000
bu=pd.read_csv("../data/sumRel.tsv",sep='\t',header=0)
bu['rel']=bu.apply(lambda row:valueof(row['import_val'],row['export_val']),axis=1)
newrel=bu.drop(['export_val','import_val'],axis=1,inplace=False)
newrel.to_csv("Ecorel.tsv",sep='\t')
#gr=bu[['dest','rel']].groupby(bu['origin'])
d=dict()
for idx,row in bu.iterrows():
    org=row['origin']
    des=row['dest']
    rel=row['rel']
    d.setdefault(org,{}).update({dest: rel})
with open("../data/EcoRel.json","w") as f:
    json.dump(d,f)
