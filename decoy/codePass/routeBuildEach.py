import json
import os,sys
import concurrent.futures
import time
def buildindex():
    path=dict()
    with open("../data/ShortestPath.json","r") as f :
        path=json.load(f)
    d=dict()
    for k,v in path.items():
        for key,value in v.items():
            for i in value:
                if i in d.keys():
                    newtuple=(k,key)
                    if not newtuple in d[i]:
                        d[i].append(newtuple)
                else:
                    l=list()
                    d[i]=l
                    newtuple=(k,key)
                    d[i].append(newtuple)
                print("extending "+i)
    with open("../data/PathIndex.json","r") as f :
        json.dump(d,f)
                
def getEachRoute(start,end):
	l=list()
	with open("../data/caslist.json","r") as f:
        	l=json.load(f)
	path=dict()
	with open("../data/ShortestPath.json","r") as f:
		path=json.load(f)
	for ll in l[start:end]:
		fn=ll+"-init-route.json"
		if not os.access(fn,os.F_OK):
			print("building "+fn+"route")
			result=list()
			for k in path.keys():
				for kk in path[k].keys():
					if ll in path[k][kk]:
						result.append(path[k][kk])
			with open(fn,"w")as f:
				json.dump(fn,f)
		else:
			print(ll+"route file already exist")
			continue
if __name__=="__main__":	
	lines=[ (0,1560),
	#	(780,1560),
		(1560,3120),
	#	(2340,3120),
		(3120,4680),
	#	(3900,4680),
		(4680,6244)]
	#	(5460,6244)]
	if sys.argv[1]=="0":
		getEachRoute(lines[0][0],lines[0][1])
	elif sys.argv[1]=="1":
		getEachRoute(lines[1][0],lines[1][1])
	elif sys.argv[1]=="2":
		getEachRoute(lines[2][0],lines[2][1])
	elif sys.argv[1]=="3":
		getEachRoute(lines[3][0],lines[3][1])
	else :
		start=time.time()
		buildindex()
		print(int(time.time()-start))
#	with concurrent.futures.ProcessPoolExecutor(max_workers=4) as exe:
#		res=list(exe.map(getEachRoute,lines))
