import networkx as nx
import matplotlib.pyplot as plt
import json,os
if not os.access("ChinaAdjacent.gpickle",os.F_OK):
    rg=dict()
    G=nx.DiGraph()
    count=0
    with open("ChinaCentral.json","r") as f :
        rg=json.load(f)
    l=list(rg.keys())
    for key,value in rg.items():
        G.add_node(key)
        for v in value:
            if v in l:
                print("src:"+key+"des:"+v)
                G.add_node(v)
                G.add_edge(key,v)
           # count+=1
    print("finish G build,to draw")
#print(count)
    print(G.size())
    nx.draw(G,pos=nx.spring_layout(G,scale=3))
    nx.write_gpickle(G,"ChinaAdjacent.gpickle")
else:
    G=nx.read_gpickle("ChinaAdjacent.gpickle")
path=dict()
if not os.access("ShortestPath.json",os.F_OK):
    with open("ShortestPath.json","r") as f:
        path=json.load(f)
print(len(path))
print("draw finish")
plt.savefig("topo.png") 
