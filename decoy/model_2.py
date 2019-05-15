import sys
sys.path.append("./Decoy")
from Decoy import DS_AS
from Decoy import DS_Caculate as method 
from Decoy import DS_Global as glb
from Decoy import DS_Censor as cen
import json
def select(ASes,cen,CGR,P):
    while True :
        #get AS react set
        AdRecord=None
        Ad=ASes.getEachASResponse(CGR,P)
        if Ad.size>AdRecord.size :
            ratio=Ad.inter(AdRecord).size/Ad.union(AdRecord).size
        else :
            ratio=A_d.inter(Ad).size/A_d.union(Ad).size
            Ac=cen.response(ASes.getDecoyAS())
        # until it's stablity reach our design
        if ratio<glb.Stabilty:
            EQ=refineEQ(ASes,Ad.inter(A_d),Ac)
            return EQ
        else:
            AdRecord=Ad
def refineEQ(ASes,inter,R):
	selected=ASes
	rAd=ASes
	rAc=R
	Converged=False
	History=ASes
	while not Coverged :
		rAd=AS_act.get()
		rAc=cen.response()
	if not Ad.contain(Selected):
		if not Selected.equal(Ad) :
			Selected=Ad
		History=selected
	if History.contain(Ad):
		Coveraged=True
	History.append(Ad)
	return Selected,Ac 
if __name__=="__main__":
    glb._init()
    ASes=DS_AS.ASset()
    ASes.build_init(glb.ChinaGeoLoc_Relate,glb.EcoRel,glb.Paths)
    print("init result:"+str(len(ASes_init.ASs))+"from model_2")
    decoyinit=list()
    with open("output/game1Decoy.json","r") as f:
        decoylist=json.load(f)
    censor=cen.censor(glb.Paths,decoyinit,glb.G)
    select(ASes,censor,glb.ChinaGeoLoc_Relate,glb.Paths)
    
    
