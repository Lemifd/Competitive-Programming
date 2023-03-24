class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        hashmap=set()
        for i in range(len(nums)):
            if len(hashmap)==k+1:
                hashmap.remove(nums[i-k-1])
            if nums[i] in hashmap:
                return hashmap
            hashmap.add(nums[i])
        return False

nums =[1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums,k))