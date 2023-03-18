class Solution:
    def isCovered(self, ranges, left: int, right: int):
        a=[x for x in range(left,right+1)]
        for i,k in ranges:
            for i in range(i,k+1):
                pass
            if right in range(i,k+1):
                re=True

        
    

nums=[[37,49],[5,17],[8,32]]

print(Solution().isCovered(nums,29,49))