import pandas as pd
import json,os
import DS_Global as glb
import DS_Caculate as cac
# next step design a structure ,which can find all path contains the AS,and
# caculate all sum of source AS size * distination AS size if the AS in the Route
 
class AS:
    def __init__(self,asn,size,country):
        self.size=size
        self.asn=asn
        self.geo=None
        self.decoy_flag=False
        self.benefit=None
        #self.route=route
        self.country=country
        self.cost=None
       # self.benefit()
        #self.routeBuild()
    def routeBuild(self,route):
        self.route=glb.Paths[self.asn]
    #it needs O(n^2) to get this answer
    def cost_set(self,cost):
        self.cost=cost
    def Benefit(self):
        print("caculating benefit of "+self.asn)
        for p in glb.paths:
            if p!=None:
                for pp in p:
                    if self.asn in pp:
                        self.benefit=int(glb.ChinaGeoLoc_Relate[pp[1]]['size'])*int(glb.ChinaGeoLoc_Relate[pp[-1]]['size'])
            #self.benefit=r[1].sizer[-1].size
#       BENEFIT=SUM(ds_SIZE*sr_SIZE)

#def SetASset():
#    parse=pd.read_csv('ASdataTest.csv',sep='\t',header=0)
#    return AS
def getBenefit(elem):
    return elem.benefit
def getBenefitR(elem):
    return elem.benefit/elem.cost
class ASset:
    def __init__(self):
        self.ASs=set()
        self.size=0
        self.AS_dict=None
        self.costsum=0
    # used for build an as set
    def getASList(self):
        return list(self.ASs)
    def cost(self):
        aslist=list(self.ASs)
        for i in aslist:
            self.costsum=self.costsum+i.cost
    def build_init(self):
        print(len(glb.ChinaGeoLoc_Relate))
        if not len(glb.ChinaGeoLoc_Relate)==0:
            for key,value in glb.ChinaGeoLoc_Relate.items():
                a=AS(key,value['size'],value['Country_N'])
                print(type(a))
                c=cac.Cost_AS(a)
                a.Benefit()
                a.cost_set(c)
                self.ASs.add(a)
    def addAS(self,AS):
        self.ASs.add(AS)
        self.size=self.size+1
    #get max benefit
    def getMaxBenefitAS(self):
        Aslist=list(self.ASs)
        temp=-1
        loc=-1
        for idx,val in enumerate(Aslist):
            if val.benefit/val.cost >temp :
                temp=val.benefit/val.cost
                loc=idx
        self.ASs.discard(Aslist[loc])
        return Aslist[loc]
    def getMaxBenefitRateAS(self):
        Aslist=list(self.ASs)
        temp=-1
        loc=-1
        for idx,val in enumerate(Aslist):
            if val.benefit>temp :
                temp=val.benefit
                loc=idx
        self.ASs.discard(Aslist[loc])
        return Aslist[loc]
       # Aslist.sort(key=getBenefitR,reverse=True)
       # return Aslist[0]
    #for game two
    def inter(self,Ad):
        return self.ASs.intersection(Ad)          
    def union(self,Ad):
        return self.ASs.union(Ad)
if __name__=="__main__":
    glb._init()
    ASS=ASset()
    ASS.build_init()
    print(ASS.getASList())
