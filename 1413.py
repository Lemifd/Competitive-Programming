class Solution:
    def minStartValue(self, nums) -> int:
        # _sum=[]
        # for i in range(len(nums)):
        #     if i==0:
        #         _sum.append(nums[i])
        #         continue
        #     _sum.append(nums[i]+_sum[-1])
        # print(_sum)
        # return 1 if min(_sum) >0 else abs(min(_sum))+1
        sumv=0
        minv=0
        for i in range(len(nums)):
            sumv+=nums[i]
            if sumv< minv:
                minv=sumv
        return abs(minv) + 1
        




nums = [-3,2,-3,4,2]
# nums = [1,2]
# nums = [1,-2,-3]
# nums=[0]
# nums=[2,3,5,-5,-1]
print(Solution().minStartValue(nums))