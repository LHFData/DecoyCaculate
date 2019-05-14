import DS_Route
import pandas as pd
import numpy as np
import json
import copy

# this module include RAD simulation and RIB build

class RouteInformationBase:
    def __init__(self,filename):
        self.topo=pd.read_csv(filename,sep='\t',header=0)
        self.graph=None
        self.paths=dict()
        self.aslist=list(self.topo['src'].drop_duplicates())
    
    def updateGraph(self,src,des,rel):
        if rel==0:
            self.graph[src].append(des)
            self.graph[des].append(src)
        else:
            self.graph[src].append(des)
    #get topology graph adjacent list
    def build(self):
        self.graph=dict()
        for index,row in self.topo.iterrows():
            if row['src'] in self.graph:
                if row['des'] in self.graph:
                    self.updateGraph(row['src'],row['des'],row['rel'])
                else:
                    self.graph[row['des']]=list()
                    self.updateGraph(row['src'],row['des'],row['rel'])
            else:
                self.graph[row['src']]=list()
                if row['des'] in self.graph:
                    self.updateGraph(row['src'],row['des'],row['rel'])
                else:
                    self.graph[row['des']]=list()
                    self.updateGraph(row['src'],row['des'],row['rel']) 
            print(str(index)+"/"+str(len(self.topo)))
        print("build AS topology graph finish")
    #get shortest routing without revenue took into consideration
    def routeFinding(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        if not start in self.graph:
            return None
        shortest=None
        for node in self.graph[start]:
            if node not in self.graph[start]:
                newpath=self.routeFinding(node,end,path)
                if newpath:
                    shortest=newpath
        return shortest 
    #get all reachable AS path as routing
    def routebuild(self,start,end,path=[]):
         path=path+[start]
         if start==end:
            return [path]
         if not start in self.graph:
            return []
         paths=[]
         for node in self.graph[start]:
             if node not in path:
                 newpaths=self.routebuild(node,end,path)
                 for newpath in newpaths:
                     paths.append(newpath)
         return paths
    #get all route
    def routeinit(self):
        for i in self.aslist:
            for j in self.aslist:
                route=self.routebuild(i,j)
                if len(route)!=0:
                    if i in self.paths:
                        self.paths[i].append(route)
                    else:
                        self.paths[i]=list()
                        self.paths[i].append(route)
    def dump(self,ds_type):
        if ds_type=='l' :
            with open('routelist.json','w') as f:
                json.dump(self.aslist,f)
        elif ds_type=='g' :
            with open('routegraph.json','w') as f:
                json.dump(self.graph,f)
        else:
            with open('routepaths','w') as f:
                json.dump(self.graph,f)
    #each route need to be evaluate its benefit and its des 
    #
    
class Decision:
    def __init__(self,Path,Decoy_Flag,Bussiness):
        self.path=Path
        self.prefer=None
        self.transitfee=None
        self.NVF=None
        self.length=len(Path)
        self.bussiness=Bussiness
        if Decoy_Flag==1:
            self.decoy=True
        else:
            self.decoy=False
    #transifee need to be valuate by the value and ipsize each AS it go through
    def revenue(self):
        for i in path:
            self.transifee=self.transifee+1
class Censor:
    def __init__(self,Budget,Bussiness,CensorName,CensorASes):
        self.budget=Budget
        self.bussiness=Bussiness
        self.censorName=CensorName
        self.censorASes=CensorASes
        self.decision=dict()
        for cas in CensorASes:
            self.decision[cas]=list()
    def RAD(self,RIB,decoyASes):
        if len(RIB.paths)==0:
            print("init route first,please")
            return None
        else:
            for c_as in CensorASes:
                for path_cas in RIB.paths[c_as]:
                    for d_as in DecoyASes:
                        if d_as in path_cas:
                            self.decision[c_as].append(Decision(path_cas),1)
                        else:
                            self.decision[c_as].append(Decision(path_cas),0)

        
if __name__=='__main__':
    rib=RouteInformationBase("ASNtopo.tsv")
    rib.build()
    rib.routeinit()
    rib.dump('l')
    rib.dump('g')
    rib.dump('p')
