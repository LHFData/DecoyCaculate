import redis
import os
host='localhost'
port=6379

pool = redis.ConnectionPool(host=host,port=port)
r=redis.Redis(connection_pool=pool)

r.hset('p_info','name','liaohaifeng')
r.hset('p_info','age','22')
r.hset('p_info','gender','M')

r.hmset('info_2',{'name':'liaohaifeng','species':'mouse'})
print(r.hget('p_info','name').decode())
print(r.hmget('p_info',['name','age','gender']))

print(r.hgetall('p_info'))

print(r.hlen('p_info'))

print(r.hkeys('p_info'))
print(r.hvals('p_info'))

print(r.hexists('p_info','name'))
print(r.hexists('p_info','job'))

r.hdel('p_info','gender')
#print(r.hgetall('p_info'))
d=r.hgetall('p_info')
#print(type(d))
for (key,value) in d.items():
    print(key.decode(),value.decode())

print(r.hscan('p_info',cursor=0))
print(r.hscan('p_info',cursor=0,match='n*'))
