from collections import Counter
class Solution:
    def divideArray(self, nums) -> bool:
        # hasht={}
        # for i in nums:
        #     if i not in hasht:
        #         hasht[i]=1
        #     else:
        #         hasht[i]+=1

        # for i in hasht:
        #     if hasht[i]%2!=0:
        #         return False
        # return True
        count = Counter(nums)
        return all(v % 2 == 0 for v in count.values())
    
nums = [3,2,3,2,2,2]
print(Solution().divideArray(nums))