#done 2way
class Solution:
    def pivotIndex(self, nums) -> int:
        # for i,j in enumerate(nums):
        #     if sum(nums[:i])==sum(nums[i+1:]):
        #         return i
        # return -1
        su=sum(nums)
        left=0
        for i,j in enumerate(nums):
            su=su-j 
            if left==su:
                return i
            left=left+j
           
        return -1

nums = [1,7,3,6,5,6]    
print(Solution().pivotIndex(nums))

    