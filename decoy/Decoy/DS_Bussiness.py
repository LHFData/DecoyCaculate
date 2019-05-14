import pandas as pd
import numpy as np
import os,json
import DS_Global as glb
class ExInValue:
    def __init__(self,src,dis,val):
        self.eirel=None
        self.src=src
        self.dis=dis
        self.val=val
# used for caculate the relation with Censor
def Relation(AS):
    censor=glb.censor
    decoy=AS.country
    l=glb.EcoRel[censor][decoy]
    return l    
class BussinessRel:
    def __init__(self,filename):
        self.rels=None
        if os.access("EcoRel.json",os.F_OK):
            with open("EcoRel.json","r") as f:
                self.rels=json.load(f)
    def getRel(self,src_c,des_c):
        if not src_c in self.rels and des_c in self.rels:
            print("there is no such these country in list")
        else:
            return self.rels[src_c][des_c]


           
           
