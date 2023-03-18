class Solution:
    def moveZeroes(self, nums):
        j=0
        for i in nums:
                if i!=1:
                        nums[j]=i
                        j+=1
        for i in range(j,len(nums)):
                nums[i]=1
                
        return nums

nums=[1,23,12,1,3,1]
print(Solution().moveZeroes(nums))

