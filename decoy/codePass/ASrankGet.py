import requests as rq
import json
import os
import pandas as pd 
import numpy as np
import time

def randtime():
    time.sleep(0.01)
url='http://as-rank.caida.org/api/v1/asns'
data={}
headers={'Accept':'application/json'}
inf=pd.read_csv('GeoLoc.csv',sep='\t',header=0,names=['asn','size','Country_N','Country','lati','longi'])
out=pd.DataFrame(columns=['asn','size','Country_N','Country','lati','longi'])
#with open('testAS.txt','w+') as f:
#progress=ProgressBar()
if inf.empty :
    start=1
else :
    start=int(inf.tail(1)['asn'].values[0])+1
    print('start from '+str(start))

for i in range(start,65535):
    r=rq.get(url+'/'+str(i),headers=headers)
    j=r.json()['data']
    if j :
        asn=j.get('id','NaN')
        print("loading "+str(asn)+" in csv "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        size=j.get('cone').get('addresses','NaN')
        Country_N=j.get('country_name','NaN')
        Country=j.get('country','NaN')
        lati=j.get('latitude','NaN')
        longi=j.get('longitude','NaN')
        outLine=out.append(pd.DataFrame({'asn':[asn],'size':[size],'Country_N':[Country_N],'Country':[Country],'lati':[lati],'longi':[longi]}),ignore_index=True)
        randtime()
        if start==1 :
            outLine.to_csv('GeoLoc.csv',sep='\t',mode='a',index=0,header=0)
        else:
            outLine.to_csv('GeoLoc.csv',sep='\t',mode='a',index=0,header=False)
    else:
        continue


