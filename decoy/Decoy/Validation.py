import numpy as np
import networkx as nx
import matlibplot
import json

def dumpData(filename,ds):
	with open(filename,"r") as f:
		json.dump(ds,f)
