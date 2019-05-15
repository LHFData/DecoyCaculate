import pandas as pd
import json

geo=pd.read_csv("../data/ASNGeo.tsv",sep='\t',names=['asn','size','Country_N','Country','lati','longi'])
geo=geo.set_index(['asn'])
d=geo.to_dict(orient='index')
with open("GeoLoc.json","w") as f:
    json.dump(d,f)

