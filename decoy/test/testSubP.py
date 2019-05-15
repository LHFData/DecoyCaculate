from subprocess import Popen,PIPE
import select
import fcntl,os
import time
signal(SIGPIPE,SIG_DFL)
class CBGP(object):
    def __init__(self,args,server_env=None):
        if server_env:
            self.process=Popen(args,stdin=PIPE,stdout=PIPE,stderr=PIPE,env=server_env)
        else:
            self.process=Popen(args,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        flagsOut=fcntl.fcntl(self.process.stdout,fcntl.F_GETFL)
        fcntl.fcntl(self.process.stdout,fcntl.F_SETFL,flagsOut| os.O_NONBLOCK)
        
        flagsIn=fcntl.fcntl(self.process.stdin,fcntl.F_GETFL)
        fcntl.fcntl(self.process.stdin,fcntl.F_SETFL,flagsIn| os.O_NONBLOCK)
    def send(self,data,tail='\n'):
        self.process.stdin.write((data+tail).encode("GBK"))
        self.process.stdin.flush()
    def recv(self,t=.1,stderr=0):
        r=''
        pr=self.process.stdout
        while True:
            if not select.select([pr],[],[],0)[0]:
                time.sleep(t)
                continue
            r=pr.read()
            return r.rstrip()
        return r.rstrip()
if __name__=="__main__":
    srv_args='cbgp'
    cbgp=CBGP(srv_args)
    test_data='bgp load topology lhf.txt','bgp topology policies'
    for d in test_data:
        cbgp.send(d)
        print(cbgp.recv().decode("GBK"))
