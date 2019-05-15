import DS_Route
import DS_Global as glb
import DS_Bussiness as bus

def U(ASsetlist):
    decoySize=0
    Size=0
    for key,value in glb.Paths.items():
        #censor dest
        if key in glb.ChinaASList:
        #all dest to free
            for v in value.keys():
                if not v in glb.ChinaASList:
                    if v in ASsetlist:
                        #in decoy set
                        decoySize=decoySize+glb.ChinaGeoLoc[key]['size']*glb.ChinaGeoLoc_Relate[v]['size']
                    else:
                        #not in 
                        Size=Size+glb.ChinaGeoLoc[key]['size']*glb.ChinaGeoLoc_Relate[v]['size']
    return int(decoySize/(Size+decoySize))
def U(ASsetlist,P,CGL,CAL,CGR):
    decoySize=0
    Size=0
    for key,value in P.items():
        #censor dest
        if key in CAL:
        #all dest to free
            for v in value.keys():
                if not v in CAL:
                    if v in ASsetlist:
                        #in decoy set
                        decoySize=decoySize+CGL[key]['size']*CGR[v]['size']
                    else:
                        #not in
                        Size=Size+CGL[key]['size']*CGR[v]['size']
    if decoySize==0:
        return 0
    else:
        return int(decoySize/(Size+decoySize))


def Cost_AS(AS,P):
    return glb.p0*AS.size*bus.Relation(AS,P)
#input.ASset
def getRouteOfAS(Paths,ASN):
    result=list()
    for p in Paths:
        for pp in p:
            if ASN in pp:
                result.append(pp)
    return result
def U_ASn(ASlist,AS):
    utility=0
    for key,values in glb.Paths.items():
        #censor start 
        if key in glb.ChinaASList:
            for k,v in values.items():
                #free dest
                if not k in glb.ChinaASList:
                    #independent AS in this path
                    if AS.asn in v:
                        #no decoy in this path before
                        if ASList.count(k)==0:
                            utility=utility+glb.ChinaGeoLoc[key]['size']*glb.ChinaGeoLoc_Relate[k]*(1+glb.dtransfee)   
                        #already have one
                        else:
                            utility=utility+glb.ChinaGeoLoc[key]['size']*glb.ChinaGeoLoc_Relate[k]
    return utility
                           
def Cost_ASset(aslist):
    sum_cost=0
    for a in aslist:
        sum_cost=sum_cost+a.cost
    return sum_cost


def Benefit_1(AS,PathSet,Route):
    benefit_as=0
    for x in PathSet.findAS(AS):
        if Route.find(AS,src,dis) :
       	    benefit=src.size*dis.size
            benefit_as=benefit_as+benefit
        else:
            benefit_as=benefit_as+0
def Benefit_2(AS,PathSet,Route):
     Benefit_as=Benefit_1(AS,PathSet,Route)/Cost_AS(p0,AS,relation)

if __name__== '__main__':
    
    print(Cost_AS)
