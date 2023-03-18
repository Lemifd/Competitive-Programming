class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        for index,val in enumerate(nums):
            if val in nums[index+1:index+1+k]:
                return True
        return False







nums = [1,0,1,1]
k = 1
print(Solution().containsNearbyDuplicate(nums,k))