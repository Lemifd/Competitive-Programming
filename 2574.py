class Solution:
    def leftRigthDifference(self, nums):
        total=sum(nums)
        ans=[]
        leftsum=0
        for i in range(len(nums)):
            leftsum+=nums[i]
            rightsum=abs(total-leftsum)
            ans.append(abs(leftsum-nums[i]-rightsum))
        return ans


nums = [10,4,8,3]
print(Solution().leftRigthDifference(nums))