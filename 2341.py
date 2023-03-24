from collections import Counter 
class Solution:
    def numberOfPairs(self, nums):
        pair=0
        for i in Counter(nums).values():
            pair+=i//2
        return [pair,len(nums)-2*pair]
nums = [1,1,1,2]

print(Solution().numberOfPairs(nums))
