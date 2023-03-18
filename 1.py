#done
class Solution:
    def twoSum(self, nums, target: int):
        ans=[]
        for index,val in enumerate(nums):
            if target-val in nums:
                ans.append(index)
        print(ans)
        for index,val in enumerate(nums):
            if target-nums[ans[0]] in nums and target-nums[ans[0]]!=nums[ans[0]]:
              return [index,target-nums[ans[0]]]
        

nums = [4,3,1,5,6]
target = 6
print(Solution().twoSum(nums,target))