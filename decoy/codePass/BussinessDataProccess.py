import pandas as pd
import numpy as np
import os,json 
def create():
	country_name=pd.read_csv('country_names.tsv',sep='\t',header=0)
	new_country_name=country_name.drop(['id'],axis=1,inplace=False)
	dict_country=new_country_name.set_index('id_3char').T.to_dict('list')
	iovalue=pd.read_csv('year_origin_destination_hs07_4.tsv',sep='\t',header=0)
	gr1=iovalue[['export_val','import_val']].groupby([iovalue['origin'],iovalue['dest']])
	output=gr1.sum().reset_index()
	for index,row in output.iterrows():
		if row['origin'] in dict_country:
			output.loc[index,'origin']=dict_country[row['origin']]
		if row['dest'] in dict_country:
			output.loc[index,'dest']=dict_country[row['dest']]
	output.to_csv('sumRel.tsv',sep='\t',index=0)
def getChinaEco():
	cl=list()
	gl=dict()
	if os.access("../data/caslist.json",os.F_OK):
		#cl=list()
		with open("../data/caslist.json","r")as f:
			cl=json.load(f)
	else:
		print("miss country related aslist")
		return
	if os.access("../data/GeoLoc.json",os.F_OK):
		with open("../data/GeoLoc.json","r")as f:
			gl=json.load(f)
	else:
		print("miss GeoLoc data")
		return
	sumEco=pd.read_csv('../data/new_val_rel.tsv',sep='\t',header=0)
	if not os.access("../data/c_GeoLoc.json",os.F_OK):
		c_rel_GL=dict()
		for key,value in gl.items():
			if key in cl:
				c_rel_GL[key]=gl[key]
		with open("../data/c_GeoLoc.json","w") as f:
			json.dump(c_rel_GL,f)
        #you need to finish the related as's bussiness realation 
	
if __name__=="__main__":
	getChinaEco()
