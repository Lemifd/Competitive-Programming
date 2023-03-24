class Solution:
    def findGCD(self, nums) -> int:
        _min,_max=min(nums),max(nums)
        if _max%_min==0:
            return _min
        for i in range(_min-1,0,1):
            if _min%i==0 and _max%i==0:
                return i
        return 1
nums = [7,5,6,8,3]
print(Solution().findGCD(nums))