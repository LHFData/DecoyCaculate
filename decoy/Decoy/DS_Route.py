import DS_Global as glb
class Route:
    def __init__(self,src,dis):
        self.src=src
        self.dis=dis
        self.decoy_flag=0
        #route of AS
        self.routepath=set()
        self.censor_num=0
        self.decoy_num=0
    def addMid(midAS):
        set.add(midAS)
        if midAS.cen_flag :
            self.censor_num=self.censor_num+1
        else :
            self.decoy_num=self.decoy_num
    def findAS(AS):
        if AS in self.routepath :
           return 1
        else :
           return 0
    def find(AS,src,dis):
        return 0
class RouteSet:
    def __init__(self):
        self.count=len(glb.Paths)
        self.route_dic={}
        '''if os.access("route.json",os.F_OK):
            with open("route.json","r") as f:
                self.route_dic=json.load(f)
        else:
            print("miss route.json")'''
#    def buildRoute(self):
#        objectdict=dict{}
#        for key,value in self.route_dic.items():

    def add(self,Route):
        self.count=self.count+1
        self.route_dic[str(self.count)]=Route
    def containRFind(self,AS):
        RouteContain=list()
        for Route in self.route_dic.values():
            if AS in Route.routepath:
                RouteContain.append(Route.routepath)
    def getAll(self):
        for k,x in self.route_dic.items():
            print(k,x.src,x.dis)

