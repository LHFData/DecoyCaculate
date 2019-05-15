import subprocess as sp
import fcntl,os
def outputResult(output):
    for o in output:
        print(o.decode("GBK"))
cbgp=sp.Popen('cbgp',stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE,shell=True)
flags=fcntl(cbgp.stdout,fcntl.F_GETFL)
fcntl.fcntl(cbgp.stdout,fcntl.F_SETFL,flags | os.O_NONBLOCK)
#fl=fcntl.fcntl(fd,fcntl.F_GETFL)
#fcntl.fcntl(fd,fcntl.F_SETFL|os.O_NONBLOCK)
cbgp.stdin.write('bgp topology load to.txt'.encode("GBK"))
cbgp.stdin.flush()
try:
    while True:
        line=cbgp.stdout.readline()
        if line:
            print(line.strip())
        else:
            print("no data")
except KeyboardInterrupt:
    print("killing")
#output=cbgp.stdout.readlines()
#for out in output:
#out=cbgp.communicate(input='bgp topology load to.txt'.encode("GBK"))
#    outputResult(out)
#out=cbgp.communicate(input='bgp topology policies'.encode("GBK"))
#outputResult(out)
#if __name__= '__main__':
#    try:
     
