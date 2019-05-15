import pandas as pd
import numpy as np

topo=pd.read_csv('topology.txt',sep='\t',header=0)
out=pd.DataFrame(columns=['src','des','rel'])
#topo[(topo.des<65535)&(topo.src<65535)].to_csv('topo.tsv')
for index,row in topo[(topo.des<65535)&(topo.src<65535)].iterrows():
    
    if row['rel']==-1:
        src=row['des']
        des=row['src']
        rel=1
    #    out=out.append(pd.DataFrame({'src':[src],'des':[des],'rel':[rel]}),ignore_index=True)
    else: 
        src=row['src']
        des=row['des']
        rel=row['rel']
    out=out.append(pd.DataFrame({'src':[src],'des':[des],'rel':[rel]}),ignore_index=True)
 
out.to_csv('to.txt',sep='\t',index=0)
        #temp=row['src']
        
        #row.replace(row['src'],row['des'])
        #row.replace(row['des'],temp)
        #row.replace(row['rel'],1)
        #print(type(row),type(row['src']))
#for index,row in topo[(topo.des<65535)&(topo.src<65535)].iterrows():
#    print(row,100)
#print(topo)

#topo.to_csv('t.txt')
