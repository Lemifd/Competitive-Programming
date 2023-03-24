class Solution:
    def countKDifference(self, nums, k) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               if nums[i]+k== nums[j] or nums[i]-k==nums[j]:
                c+=1
        
        return c
    


nums = [1,2,2,1]
k = 1
print(Solution().countKDifference(nums,k))