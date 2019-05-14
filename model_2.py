import sys
def model2():
    while True :
        Ad=AS_act.get()
        if Ad.size>A_d.size :
            ratio=Ad.inter(A_d).size/Ad.union(A_d).size
        else :
            ratio=A_d.inter(Ad).size/A_d.union(Ad).size
            Ac=CBGP.res
        if ratio<t then
            EQ=refineEQ(Ad.inter(A_d),Ac)
            return EQ
        A_d=Ad
def refineEQ(ASes,R):
	selected=ASes
	rAd=ASes
	rAc=R
	Converged=False
	history=ASes
	while !Coverged do
	    rAd=AS_act.get()
	    rAc=CBGP.res
	if !Ad.contain(Selected):
		if !Selected.equal(Ad) :
                    Selected=Ad
		History=selected
	if History.contain(Ad):
		Coveraged=True
	History.append(Ad)
     Return Selected,Ac 
