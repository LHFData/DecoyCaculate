import sys
sys.path.append("./Decoy")
from Decoy import DS_AS
from Decoy import DS_Caculate as method 
from Decoy import DS_Global as glb
from Decoy import DS_Censor as cen
import pdb
import json
def select(ASes,cen,CGR,P,decoylist):
	flag=0
	AdRecord=DS_AS.ASset()
	while True :
	#get AS react set
		if flag!=0:
			decoylist=ASes.getDecoyASList()
			Ad=ASes.getEachASResponse(CGR,P,decoylist)
		else:
			Ad=ASes.initGetEachASResponse(CGR,P,decoylist)
		if Ad.size>AdRecord.size :
			ratio=Ad.inter(AdRecord).size/Ad.union(AdRecord).size
		else :
			ratio=AdRecord.inter(Ad).size/Ad.union(AdRecord).size
			Ac=cen.response(ASes.getDecoyAS())
	# until it's stablity reach our design
		if ratio>glb.Stabilty:
			EQ,EC=refineEQ(ASes,Ad.inter(A_d),Ac,CGR,P,AdRecord.getDecoyASList())
			return EQ,EC
		else:
			AdRecord=Ad
			falg=flag+1
			#decoylist=ASes.getDecoyASList()
def refineEQ(ASes,inter,R,CGR,P,decoylist):
	selected=inter
	Ad=inter
	Ac=R
	Converged=False
	History=list()
	Histroy.append(inter)
	while not Coverged :
		Ad=ASes.getEachASResponse(CGR,P,decoylist)
		Ac=cen.response(ASes.getDecoyAS())
	if not Ad.contain(Selected):
		if not Selected.equal(Ad) :
			Selected=Ad
		History=History.append(Selected)
	if Ad in Histroy:
		Coveraged=True
	History.append(Ad)
	return Selected,Ac 
if __name__=="__main__":
	glb._init()
	ASes=DS_AS.ASset()
	#pdb.set_trace()
	ASes.build_init(glb.ChinaGeoLoc_Relate,glb.EcoRel,glb.Paths)
	print("init result:"+str(len(ASes.ASs))+"from model_2")
	decoyinit=list()
	with open("output/game1Decoy.json","r") as f:
		decoylist=json.load(f)
	censor=cen.censor(glb.Paths,decoyinit,glb.G)
	ad,ac=select(ASes,censor,glb.ChinaGeoLoc_Relate,glb.Paths,decoyinit)
	for d in ad:
		print(d.asn)
	for d in Ac:
		print(d.asn)
    
