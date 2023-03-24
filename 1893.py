class Solution:
    def isCovered(self, ranges, left: int, right: int):
        list=[i for i in range(left,right+1)]
        for i,j in ranges:
            k=0
            while k<len(list):
                if i<=list[k]<=j:list.pop(k)
                else:k+=1
            if not list:return True
        return list
        

ranges =[[37,49],[5,17],[8,32]]

left = 29
right = 49

print(Solution().isCovered(ranges,left,right))