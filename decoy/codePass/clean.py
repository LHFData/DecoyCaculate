import math
import json
import numpy as np
import sys
def meanofSize():
	l=list()
	d=dict()
	with open("../data/c_GeoLoc.json","r")as f :
		d=json.load(f)
	for k,v in d.items():
		if not math.isnan(v["size"]):
			l.append(v["size"])
	result=np.mean(l)
	return result
def insteadForMean(i):
	d=dict()
	with open("../data/c_GeoLoc.json","r")as f:
		d=json.load(f)
	for k,v in d.items():
		if math.isnan(v["size"]):
			v["size"]=i
	with open("../data/c_GeoLocwithMean.json","w")as f:
		json.dump(d,f)
if __name__=="__main__":
    l=sys.argv[1]
    if l=="m":
       print(meanofSize())
    else:
       insteadForMean(int(l))
