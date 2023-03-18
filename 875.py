class Solution:
    def minEatingSpeed(self, piles, h):
        piles.sort()
        if len(piles)==h:
            return max(piles)
        summ=sum(piles)
        if summ%h==0:
            k=summ//h
        else:
            k=1+summ//h
        return self.result(piles,k,h)


    def check(self,piles,k):
            c=0
            for i in range(len(piles)):
                d=1
                while piles[i]-d*k>-k:
                    c+=1
                    d+=1
            return c
        
    def result(self,piles,k,h):
         
            start=k
            end=max(piles)

          
            while start < end:
                mid=(start+end)//2
                c=self.check(piles,mid)
                if c<=h:
                    return f"{c-1} h"
                end=mid

            
        
               

           
           
        
       
        



a=[3,6,7,11]
a1=[30,11,23,4,20]
a2=[30,11,23,4,20]
h2=6
h=8
h1=5
print(Solution().minEatingSpeed(a1,h1))
