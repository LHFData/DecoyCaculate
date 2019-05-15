import sys
from Decoy import DS_AS
from Decoy import DS_Caculate as method 
from Decoy import DS_Global as glb
from Decoy import DS_Censor as cen
def model2(ASes):
    while True :
        #get AS react set
        AdRecord=None
        Ad=ASes.getEachASResponse()
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
def refineEQ(ASes,R):
	selected=ASes
	rAd=ASes
	rAc=R
	Converged=False
	History=ASes
	while !Coverged :
	    rAd=AS_act.get()
	    rAc=cen.response()
	if !Ad.contain(Selected):
		if !Selected.equal(Ad) :
                    Selected=Ad
		History=selected
	if History.contain(Ad):
		Coveraged=True
	History.append(Ad)
     Return Selected,Ac 
if __name__=="__main__":
    glb._init()
    ASes=DS_AS.ASset()
    ASes.build_init(glb.ChinaGeoLoc_Relate,glb.EcoRel,glb.Paths)
    print("init result:"+str(len(ASes_init.ASs))+"from model_1")
    
    
