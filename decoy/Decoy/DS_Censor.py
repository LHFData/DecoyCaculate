import json
import DS_Caculate as method
import DS_AS as struct
import DS_Global as glb
import copy
import networkx as nx
import matplotlib as plt
class censor:
    def __init__(self,P,DecoySetList,G):
        #a route path which is reliable
        self.decision=copy.deepcopy(P)
        self.currentDecoy=DecoySetList
        self.G=G
        self.pathlen=dict()
        self.getPathLen(P)
    def getPathLen(self,P):
        for p in P.keys():
            for pp in P[p].keys():
                self.pathlen[p]=dict()
                self.pathlen[p][pp]=len(P[p][pp])
    def routeRefind(self):
        for d in self.currentDecoy:
            self.G.remove_nodes(d)
        self.decision=nx.all_shortest_path(G)
    def decision(self):
        lofd=list(self.decision.keys())
        for dk in lofd:
            llofd=list(self.decision[dk].keys())
            for dkk in llofd:
                if dkk in self.currentDecoy:
                    del(self.decision[dk][dkk])
    #def transitfee(self):
    def unreachabelRate():
        oldLen=self.reachableNum
        self.reachable()
        if oldLen!=0 and self.Len!=0:
            return oldLen/self.reachableNum
        elif oldLen==0 and self.reachableNum!=0:
            return 0
        else:
            return 1
    def reachable(self):
        Len=0
        for d in self.decision:
            Len=Len+len(d)
        self.reachableNum=Len
    #def NVF(self):
    def LongerPath(self,G):
        old=self.pathlen
        new=dict(nx.shortest_path_length(G))
        com=list(old.keys()-new.keys())
        self.lenchange=dict()
        for c in com:
            comm=list(old[c].keys()-new[c].keys()) 
            for cc in comm:
                temp=dict()
                temp[cc]=old[c][cc]-new[c][cc]
                self.lenchange[c]=temp        
