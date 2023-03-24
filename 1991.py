class Solution:
    def findMiddleIndex(self, nums) -> int:
        r=sum(nums)
        l=0
        for i,val in enumerate(nums):
            r-=val
            if r==l:
                return i
            l+=val
        return -1

# nums = [2,3,-1,8,4]
# nums = [1,-1,4]
nums = [2,5]
print(Solution().findMiddleIndex(nums))