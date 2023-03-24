class Solution:
    def minimumOperations(self, nums) -> int:
        # c=0
        # while False==all(v ==0 for v in nums):
        #     min=10**5
        #     for i in nums:
        #         if i!=0 and i<min:
        #             min=i
        #     for i in range(len(nums)):
        #         if nums[i]>0:
        #             nums[i]-=min
        #         if nums[i]<0:
        #             nums[i]=0
        #     c+=1

        # return c
         return len({num for num in nums if num != 0})
            

nums = [1,5,0,3,5]
print(Solution().minimumOperations(nums))