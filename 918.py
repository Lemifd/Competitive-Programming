class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        maxSum=-3*10**4
        curr=0
        go=True
        i=0
        while go:
            if i==len(nums):
                for i in nums:
                    curr+=nums[len(nums)-i]
                    if curr>maxSum:
                        maxSum=curr
                    if curr<0:
                        return maxSum
            curr+=nums[i]
            if curr>maxSum:
                maxSum=curr
            if curr<0:
                curr=0
            i+=1

n= [5,2,5]


print(Solution().maxSubarraySumCircular(n))
        
    