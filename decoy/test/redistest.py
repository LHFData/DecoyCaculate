import redis
import os
import pickle
import json
class liuyilin(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
def liuyilin2dict(lyl):
    return {
        'name':lyl.name,
        'age':lyl.age
    }
def dict2liuyilin(d):
    return liuyilin(d['name'],d['age'])
r=redis.Redis(host='localhost',port=6379,db=0)
#r.set('lhf','fuck')
a=liuyilin('lyl',20)
r.set('test',json.dumps(liuyilin2dict(a)))
b=r.get('test')
#print(b)
c=json.loads(b,object_hook=dict2liuyilin)
print("name:"+str(c.name)+"age:"+str(c.age))
#fs=open('lhf.txt','wb')
#fs.write(r.get('lhf'))
