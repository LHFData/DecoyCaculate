import DS_Caculate as cac
d={"1":
      {"2":
           ["1","3","2"]
      },
   "2":
      {"3":
           ["2","4","3"],
       "4":
           ["2","5","4"]
      }
   }
l=cac.getRouteOfAS(d,"3")
print(l)
class lhf:
	def __init__(self,num):
		self.num=num
