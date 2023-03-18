class Solution:
    def rotate(self, nums,k):
        """
        Do not return anything, modify nums in-place instead.

        """
        # for i in range(k):
        #         nums.insert(0,nums[len(nums)-1])
        #         del nums[len(nums)-1]
        tep=nums[-k:]
        del nums[-k:]
        for i in range(len(tep)-1,-1,-1):
                nums.insert(0,tep[i])

        print(nums)
# a=[x for x in range(1,8)]
a= [1,2,3,4,5,6,7]
k = 3
print(a)
Solution().rotate(a,k)