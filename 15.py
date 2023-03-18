class Solution:
    def threeSum(self, nums):
        ans=[]
        for i in nums:
                if -1*i - i in nums:
                    ans.append([val,i,-1*val-i])
        return ans
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum(nums))