#/!usr/bin/python
import sys
sys.path.append("./Decoy")
from Decoy import DS_AS 
from Decoy import DS_Route as struct
from Decoy import DS_Caculate as method
from Decoy import DS_Global as glb
#from Decoy.DS_Route import ASset,AS
def game_one(ASes,ASesR,Ad,R,A_d,F):
    while C_Decoy.get(Ad) < F :
        Select_AS=ASes.getMaxBenefitAS() 
        Ad.addAS(Select_AS)
        glb.remove(Select_AS.asn)
    while C_Decoy.get(A_d) < F :
        Select_AS_=ASesR.getMaxBenefitRateAS()
        A_d.addAS(Select_AS_)
        glb.remove(Select_AS_)
    if(U(Ad)<U(A_d)) :
        return A_d
    else:
        return Ad 
def select(ASset_init):
    ASes=DS_AS.ASset()
    while method.Cost_ASset(ASes.getASList())<F:
        Select_AS=ASset_init.getMaxBenefitAS()
        ASes.addAS(Select_AS)
        print("add"+Select_AS.asn)
        glb.remove(Select_AS.asn)
    glb.reloaddata("Paths")
    return ASes 
def selectR(ASset_init):
    ASes=DS_AS.ASset()
    while method.Cost_ASset(ASes.getASList())<F:
        Select_AS=ASset_init.getMaxBenefitRateAS()
        ASes.addAS(Select_AS)
        print("add "+Select_AS.asn)
        glb.remove(Select_AS)
    glb.reloaddata("Paths")
    return ASes
        
if __name__== '__main__':
    #load data
    glb._init()
    print(len(glb.ChinaGeoLoc_Relate))
    #load topo AS info
    ASes_init=DS_AS.ASset()
    ASes_init.build_init()
    #F/p0=10000000,F is the budget
    F=10000000
   
    Ad=select(ASes_init)
    A_d=selectR(ASes_init)
    #decoy decision
    lAd=list()
    lA_d=list()
   
    for a in list(Ad):
        lAd.append(a.asn)
    for a in list(A_d):
        lA_d.append(a.asn)
    if method.U(lAd)>method.U(lA_d):
        with open("output/game1Decoy.json","w")as f:
            json.dump(list(Ad),f)
    else:
        with open("output/game1Decoy.json","w")as f:
            json.dump(list(A_d),f)
 # ds set

# C_decoy: the cost of decoy

# F: finite buget

# B_ASes: Benefit of ASes

# ASi: The i-th AS

# A_cens: censored AS 

# A_free: free AS out of censor

# ASi_size:The size of AS(ip num,get from Dataset)

# Path(i,j):the path from ASi to ASj,directed

# R(i,j): BGP route from ASi to ASj

# P_all:all path from A_cens to A_free

# a(Path(i,j)): censor's action take for Path(i,j),two kinds of action,one for BGP,other for RBGP

# Ac=(a(P(i,j))): Censor's startegy to decide routing,focus on the Path(i,j) which are all 
# belong to P_all

# Ad:ASes which can deploy decoy

# a_k :the strategy of ASk player in gametwo ,whether to be true(for decoy) or to be false (for not decoy)

# C_profile :censor's profile   
    
    




