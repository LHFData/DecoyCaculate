import networkx as nx
import matplotlib.pyplot as plt
import json,os
import numpy as np
G=nx.read_gpickle("../data/ChinaAdjacent.gpickle")

def result():
   # pos=nx.get_node_attributes(G,'pos')
   # G.node[asn]['color']=red
    geoloc=dict()
    with open("GeoOfAS.json","r") as f:
        geoloc=json.load(f)
    pos=dict()
    for k,v in geoloc.items():
        l=np.array([v["longi"],v["lati"]],float)
        pos[k]=l
   # pos=nx.spring_layout(G)
    dmin=1
    ncenter=list(pos.keys())[0]
    for n in G.nodes():
        x,y=pos[n]
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d
    p=dict(nx.single_source_shortest_path_length(G,ncenter))
    plt.figure(figsize=(8,8))
    nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G,pos,nodelist=list(p.keys()),
                           node_size=80,
                           node_color=list(p.values()),
                           cmap=plt.cm.Reds_r)
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    plt.savefig("potedge.png")
def init():
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
if __name__=="__main__":
    result()
