import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json
def getPow(num):
    num='%g' % num
    return int(num.split('+')[1])
def dumpData(filename,ds):
	with open(filename,"r") as f:
		json.dump(ds,f)
def drawLineGraph(resultfile,kind):
	ASs=list()
	with open(resultfile,"r")as f:
		ASs=json.load(f)
	GeoLoc=dict()
	with open("../data/c_GeoLoc.json","r")as f:
		GeoLoc=json.load(f)
	if kind=="as":
		F=[8,9,10]
                numAS=[4,]

if __name__=="__main__":
	print(getPow(10))
