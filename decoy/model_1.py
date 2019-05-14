#/!usr/bin/python

import sys
from Decoy import DS_Route as DS_struct
from Decoy import DS_Caculate as DS_method
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

def game_one(B_ASes,Ad,R,A_d,F):
    while C_Decoy.get() < F :
        Select_AS=B_ASes.getmax()
        Ad.add(Select_AS)
        R.remove(Select_AS)
    while C_Decoy.get() < F :
        Select_AS_=B_ASes.getmax()
        A_d.add(Select_AS_)
        R.remove(Select_AS_)
    if(U(Ad)<U(A_dnext)) :
        return A_dnext
    return Ad


if __name__== '__main__':
    B_ASes=ASset()
    Ad=ASset()
    A_d=ASset()
    F=sys.argv[1]
    A1=AS(1,1,"china",0)
    A2=AS(3,2,"japan",1)
    A3=AS(2,3,"korea",1)
    A4=AS(4,4,"noth-korea",0)
    B_ASes.addAS(A1)
    B_ASes.addAS(A2)
    B_ASes.addAS(A3)
    B_ASes.addAS(A4)
