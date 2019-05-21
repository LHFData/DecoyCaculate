import networkx as nx
import matplotlib.pyplot as plt
import json,os
import numpy as np
G=nx.read_gpickle("../data/ChinaAdjacent.gpickle").to_undirected()

def drawSpring():
    geoloc=dict()
    with open("GeoOfAS.json","r") as f:
        geoloc=json.load(f)
    pos=dict()
#    if not os.access("pos.npy",os.F_OK):
    for k,v in geoloc.items():
        l=np.array([v["longi"]*1000,v["lati"]*1000],float)
        pos[k]=l
#    np.save("pos.npy",pos)
#    else:
#        np.load("pos.npy")
  #  with open("../data/pos.json","w")as f :
  #      json.dump(pos,f)
   # posp=nx.spring_layout(G,pos)
    #nx.draw(G,pos,node_size=10,width=0.1)
#    G=G.to_undirected()
    nx.draw_networkx_edges(G,pos,width=0.1,alpha=0.1)
    nx.draw_networkx_nodes(G,pos,node_size=10,node_color=[int(i)/65535 for i in list(pos.keys())],cmap=plt.cm.Reds_r)
    plt.rcParams['savefig.dpi']=1000
    plt.rcParams['figure.dpi']=1000
    plt.savefig("../picoutput/geoofAS.png")

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
    plt.figure(figsize=(10000,10000))
    nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G,pos,nodelist=list(p.keys()),
                           node_size=10,
                           node_color=list(p.values()),
                           cmap=plt.cm.Reds_r)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.axis('off')
    plt.savefig("../picoutput/potedge.png")
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
    drawSpring()
