class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        ans=0
        for i in nums:
            if i+diff in nums and 2*diff+i in nums:
                    ans+=1
        return ans

nums = [0,1,4,6,7,10]
diff = 3
print(Solution().arithmeticTriplets(nums,diff))