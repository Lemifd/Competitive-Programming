# import bisect
class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        nums.append(10**6+1)
        _sum=[]
        for i in range(len(nums)):
            if i==0:
                _sum.append(nums[0])
                continue
            _sum.append(nums[i]+_sum[-1])
        ans=[]
        for i in queries:
            for j in range(len(_sum)):
                if _sum[j]>i:
                    ans.append(j)
                    break
                if _sum[-1]<i:
                    ans.append(len(_sum))
                    break
        return ans
        # nums.sort()
        # nums.append(10**6+1)
        # _sum=[]
        # for i in range(len(nums)):
        #     if i==0:
        #         _sum.append(nums[0])
        #         continue
        #     _sum.append(nums[i]+_sum[-1])

        # return [bisect.bisect(_sum,x) for x in queries]



nums = [4,5,2,1]
queries = [3,10,21]
# nums = [10**5]
# queries = [10**5] 
# nums = [2,3,4,5]
# queries = [1]
print(Solution().answerQueries(nums,queries))