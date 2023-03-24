class Solution:
    def a(self,grid):

        sorted_g=[sorted(x) for x in grid]
        ans=0
        while all(len(x)!=0 for x in sorted_g):
            
                _max=-10**5
                print(sorted_g)
                for i in sorted_g:
                   try:
                      last=i.pop()
                      if last > _max:
                       _max=last
                   except:
                       continue

                ans+=_max
        return ans           
grid = [[10],[1,2]]
# grid = [[1,2,4],[3,3,1]]
print(Solution().a(grid))