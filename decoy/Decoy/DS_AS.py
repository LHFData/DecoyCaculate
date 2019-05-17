import pandas as pd
import json,os
import DS_Global as glb
import DS_Caculate as cac
# next step design a structure ,which can find all path contains the AS,and
# caculate all sum of source AS size * distination AS size if the AS in the Route
 
class AS:
    def __init__(self,asn,size,country):
        print(asn)
        self.size=size
        self.asn=asn
        self.geo=None
        self.decoy_flag=False
        self.benefit=0
        #self.route=route
        self.country=country
        self.cost=None
        self.decoy_route=list()
        self.normal_route=list()
        self.cleanbenefit=0
        self.decoybenefit=0
       # self.benefit()
        #self.routeBuild()
    def routeBuild(self,P):
        print(self.asn+"getting all route through it--from DS_AS.AS.routeBuild")
        self.normal_route=cac.getRouteOfAS(P,self.asn)
       # print(self.normal_route)
    def getDecoy(self,decoylist):
        print(self.asn+"marking its decoy route--from DS_AS.AS.getDecoy")
        for r in self.normal_route:
            for rr in r:
                if rr in decoylist:
                    self.decoy_route.append(r)
        for r in self.decoy_route:
            if r in self.normal_route:
                self.normal_route.remove(r)
        
    #it needs O(n^2) to get this answer
    def cost_set(self,cost):
        self.cost=cost
    def response(self,CGR,P):
        print(self.asn+"is making its decision --from DS_AS.AS.response")
        if len(self.normal_route)!=0:
            for nr in self.normal_route:
                self.cleanbenefit=self.cleanbenefit+int(CGR[nr[0]]['size'])*int(CGR[nr[-1]]['size'])
        if len(self.decoy_route)!=0:
            for dr in self.decoy_route:
                self.decoybenefit=self.decoybenefit+int(CGR[dr[0]]['size'])*int(CGR[dr[-1]]['size'])*(1+glb.t)
        print(self.asn+"cleanbenefit:"+self.cleanbenefit+"decoybenefit:"+self.decoybenefit)
       # for p in P:
       #     if p!=None:
       #         for pp in p:
       #             if self.asn in pp:
       #                 if glb.D(pp)==1:
       #                     self.decoybenefit=self.decoybenefit+int(CGR[pp[0]['size']])*int(CGR[pp[0]['size']])*(1+glb.t*glb.D(pp))
       #                 else:
       #                     self.cleanbenefit=self.cleanbenefit+int(CGR[pp[0]['size']])*int(CGR[pp[0]['size']])
       
                        
        #self.decoyflag=True
    '''
    def Benefit(self):
        print("caculating benefit of "+self.asn)
        for p in glb.paths:
            if p!=None:
                for pp in p:
                    if self.asn in pp:
                        self.benefit=int(glb.ChinaGeoLoc_Relate[pp[1]]['size'])*int(glb.ChinaGeoLoc_Relate[pp[-1]]['size'])
            #self.benefit=r[1].sizer[-1].size
#       BENEFIT=SUM(ds_SIZE*sr_SIZE)
    '''
    def Benefit(self,CGR,P):
        print("caculating benefit of "+self.asn)
        for p in P:
            if p!=None:
                for pp in p:
                    if self.asn in pp:
                        self.benefit=self.benefit+int(CGR[pp[0]]['size'])*int(CGR[pp[-1]]['size'])
#def SetASset():
#    parse=pd.read_csv('ASdataTest.csv',sep='\t',header=0)
#    return AS
def getBenefit(elem):
    return elem.benefit
def getBenefitR(elem):
    return elem.benefit/elem.cost
class ASset:
    def __init__(self):
        self.ASs=list()
        self.size=0
        self.AS_dict=None
        self.costsum=0
        self.decoyASlist=list()
    # used for build an as set
    def initfromaslist(self,aslist):
        self.ASs=aslist
        self.size=len(aslist)
        self.decoyASlist=list()
        for i in aslist:
            if i.decoy_flag:
                self.decoyASlist.append(i.asn)
    def getASList(self):
        return self.ASs
    def cost(self):
        aslist=self.ASs
        for i in aslist:
            self.costsum=self.costsum+i.cost
    def build_init(self,CGR,ER,P):
        print("len of CGL"+str(len(CGR))+"from AS")

        print("init as set....")
        if not len(CGR)==0:
            print("strart add init AS--from DS_AS.build_init")
            for key,value in CGR.items():
                a=AS(key,value['size'],value['Country_N'])
               # print(type(a))
                c=cac.Cost_AS(a,ER)
                a.Benefit(CGR,P)
                a.cost_set(c)
                self.ASs.append(a)
                self.size=self.size+1
    def initGetEachASResponse(self,CGR,P,decoylist):
        dl=list()
        result=ASset()
        print("getting response from AS --from DS_AS")
        with open("output/game1Decoy.json","r")as f:
            dl=json.load(f)
        
        for a in self.ASs:
            print("building route of as:"+a.asn)
            a.routeBuild(P)
            a.getDecoy(decoylist)
            a.response(CGR,P)
            if a.cleanbenefit!=0 and  a.decoybenefit!=0:
                print(a.asn+"is c="+str(a.cleanbenefit)+"d="+str(a.decoybenefit))
            if a.cleanbenefit<a.decoybenefit:
                a.decoy_flag=True
                result.addAS(a)
                print("as:"+a.asn+"decide to decoy")
                self.decoyASlist.append(a.asn)
            else:
                a.decoy_flag=False
        return result
    def getDecoyAS(self):
        l=list()
        for d in self.ASs:
            if d.asn in self.decoyASlist:
                l.append(d)
        return l
    def getDecoyASList():
        return self.decoyASlist
    '''
    def build_init(self):
        print("len of CGL"+str(len(glb.ChinaGeoLoc_Relate))+"from AS")
        print("get glb.CGL"+str(len(glb.GetCGLR()))+"from AS")
     
        print("init as set....")
        if not len(glb.ChinaGeoLoc_Relate)==0:
            print("strart add init AS--from DS_AS.build_init")
            for key,value in glb.ChinaGeoLoc_Relate.items():
                a=AS(key,value['size'],value['Country_N'])
                print(type(a))
                c=cac.Cost_AS(a)
                a.Benefit()
                a.cost_set(c)
                self.ASs.append(a)
    '''
    def addAS(self,AS):
        self.ASs.append(AS)
        self.size=self.size+1
    #get max benefit
    def getMaxBenefitAS(self):
        Aslist=self.ASs
        #print(str(len(Aslist))+"is the length of as")
        temp=-1
        loc=0
        for idx,val in enumerate(Aslist):
            if val.benefit >temp :
                temp=val.benefit
                loc=idx
        self.ASs.remove(Aslist[loc])
        return Aslist[loc]
    def getMaxBenefitRateAS(self):
        Aslist=self.ASs
        temp=-1
        loc=0
        for idx,val in enumerate(Aslist):
            if val.cost==0:
                loc=idx
                break
            if val.benefit/val.cost>temp :
                temp=val.benefit/val.cost
                loc=idx
        self.ASs.remove(Aslist[loc])
        return Aslist[loc]
       # Aslist.sort(key=getBenefitR,reverse=True)
       # return Aslist[0]
    #for game two
  
    def inter(self,Ad):
        sl=set(self.ASs)
        result=ASset()
        result.initfromaslist(list(sl.intersection(set(Ad.ASs))))
        return result  
    def union(self,Ad):
        sl=set(self.ASs)
        result=ASset()
        result.initfromaslist(list(sl.union(set(Ad.ASs))))
        return result
    def contain(self,Ad):
        s=set(self.ASs)
        d=set(Ad.ASs)
        return d.issubset(s)
    def equal(self,Ad):
        if self.ASs==Ad.ASs:
            return True
        else:
            return False
if __name__=="__main__":
    glb._init()
    ASS=ASset()
    ASs=ASset()
    l=["1","2","3","6"]
    ll=["2","3","4","6"]
    for i in l:
        ASS.addAS(AS(i,32,"China"))
    for i in ASS.ASs:
        if int(i.asn)<4:
            ASs.addAS(i)
    print("result")
    print(ASs.inter(ASS).size)
    
    #ASS.build_init()
    #print(ASS.getASList())
