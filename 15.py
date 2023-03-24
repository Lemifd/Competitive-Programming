class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if -1*(nums[i]+nums[j]) in nums[j+1:]:
                    print(f"i={nums[i]} and j={nums[j]}")
                    ans.append([nums[i],nums[j],-1*(nums[i]+nums[j])])
        rans=[]
        for i in ans:
            if i not in rans:
                rans.append(i)
        return rans
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum(nums))