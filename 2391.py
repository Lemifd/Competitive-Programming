class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        # trucks={"tr1":"P","tr2":"G","tr3":"M"}
        # gar=""
        # for i in garbage:
        #     gar+=i
        # G=gar.count("G")
        # M=gar.count("M")
        # P=gar.count("P")
        # tobecollected=[P,G,M]
        # time=0
        # v=0
        # for tr,job in trucks.items():
        #     collected=0
        #     totalcollected=0
        #     for j,i in enumerate(garbage):
        #         collected=i.count(job)
        #         totalcollected+=collected
        #         time+=collected
        #         if totalcollected==tobecollected[v]:
        #             break
        #         time+=travel[j]
        #     v+=1
        # return time


   
        gar=""
        for i in garbage:
            gar+=i
        print(gar)
        time=len(gar)
        
        def ind(self,y,arr):
            for i in range(len(garbage)-1,-1,-1):
                if y in i :
                    return i
        ind()
        # for i in range(1,len(garbage)):
        #     if "M" in garbage[i]:
        #         time+=travel[i-1]
        #     if "P" in garbage[i]:
        #         time+=travel[i-1]
        #     if "G" in garbage[i]:
        #         time+=travel[i-1]
        return time



garbage = ["G","P","GP","GG"]
travel = [2,4,3]
print(Solution().garbageCollection(garbage,travel))