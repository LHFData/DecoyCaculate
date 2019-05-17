import json
import os
import pandas as pd
import networkx as nx
#import sys
#sys.paths.append("")
G=dict()
Paths=dict()
ChinaGeoLoc=dict()
ChinaASList=list()
ChinaGeoLoc_Relate=dict()
EcoRel=dict()
p0=0.0000000000001 
F=10000000000
local=""
censor="China"
decoyPath=list()
t=5
Stability=0.8
def GetPaths():
    return Paths
def GetG():
    return G
def GetCGL():
    return ChinaGeoLoc
def GetCAL():
    return ChinaASList
def GetCGLR():
    return ChinaGeoLoc_Relate
def GetER():
    return EcoRel
def _init():
	#global G
	if os.access(local+"data/ChinaAdjacent.gpickle",os.F_OK):
		global G
		print("loading G")
		G=nx.read_gpickle(local+"data/ChinaAdjacent.gpickle")
		print("load G finish")
	else:
		print("miss ChinaAdjacent.gpickle")
	#global Paths
	
	if os.access(local+"data/ShortestPath.json",os.F_OK):
		with open(local+"data/ShortestPath.json","r") as f:
			global Paths
			print("loading Paths")
			Paths=json.load(f)
			print("load Paths finish")
	else:
		print("miss ShortestPath.json")
	
	#global ChinaASList
	if os.access(local+"data/ChinaASList.json",os.F_OK):
		with open(local+"data/ChinaASList.json","r") as f:
			global ChinaASList
			print("loading ChinaASList")
			ChinaASList=json.load(f)
			print("load ChinaASList finish")
	else:
		print("miss calist.json")

	#global ChinaGeoLoc_Relate
	if os.access(local+"data/c_GeoLoc.json",os.F_OK):
		with open(local+"data/c_GeoLoc.json","r") as f:
			global ChinaGeoLoc_Relate
			print("loading ChinaGeoLoc_Relate")
			ChinaGeoLoc_Relate=json.load(f)
			print("load Paths finish")
	else:
		print("miss c_GeoLoc.json")

	#global EcoRel
	if os.access(local+"data/EcoRel.json",os.F_OK):
		with open(local+"data/EcoRel.json","r") as f:
			global EcoRel
			print("loading EcoRel")
			EcoRel=json.load(f)
			print("load EcoRel")
	else:
		print("miss EcoRel.json")
def remove(asn):
	#global Paths
	for key,value in Paths.items():
		for v in list(value.keys()):
			if asn in value[v]:
				#global Paths
				value.pop(v)
def addDecoyPath(pp):
	global decoyPath
	decoyPath.append(pp)
def getDecoyPath():
    return decoyPath
def D(pp,asn):
	if pp in decoyPath:
		return 0
	else:
		return 1
def reloaddata(data):
	print("reload data"+data)
	if data=="G":
		if os.access(local+"data/ChinaAdjacent.gpickle",os.F_OK):
			global G
			G=nx.read_gpickle(local+"data/ChinaAdjacent.gpickle")
			print("reload finish")
		else:
			print("miss ChinaAdjacent.gpickle")
	elif data=="Paths":
		if os.access(local+"data/ShortestPath.json",os.F_OK):
			with open(local+"data/ShortestPath.json","r") as f:
				global Paths
				Paths=json.load(f)
				print("reload finish")
		else:
			print("miss ShortestPath.json")
	elif data=="ChinaGeoLoc_Relate":
		if os.access(local+"data/c_GeoLoc.json",os.F_OK):
			with open(local+"data/c_GeoLoc.json","r") as f:
				global ChinaGeoLoc_Relate
				ChinaGeoLoc_Relate=json.load(f)
				print("reload finish")
		else:
			print("miss c_GeoLoc.json")
	elif data=="ChinaASList":
		if os.access(local+"data/ChinaASList.json",os.F_OK):
			with open(local+"data/ChinaASList.json","r") as f:
				global ChinaASList
				ChinaASList=json.load(f)
				print("reload finish")
		else:
			print("miss calist.json")
	elif data=="EcoRel":
		if os.access(local+"data/EcoRel.json",os.F_OK):
			with open(local+"data/EcoRel.json","r") as f:
				global EcoRel
				EcoRel=json.load(f)
				print("reload finish")
		else:
			print("miss EcoRel.json")
	else:
		print("invalid reload data")

def test():
	_init()
	#global G
	#global Paths
	#global ChinaASList
	#global ChinaGeoLoc_Relate
	#global EcoRel
	print(len(G))
	print(len(Paths))
	print(len(ChinaGeoLoc))
	print(len(ChinaGeoLoc_Relate))
	print(len(EcoRel))
if __name__=="__main__":
	test() 
