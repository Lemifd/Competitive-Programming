class Solution:
    def numIdenticalPairs(self, nums):
        #bruteforce
        #  count=0
        # for i in range(len(nums)):
        #     j=nums[i+1:]
        #     for k in j:
        #         if nums[i]==k:
        #             count+=1
        # return count
        setmap={}
        count=0
        for i in nums:
            if i not in setmap:
                setmap[i]=0
            else:
                setmap[i]+=1
        for x in setmap:
            count+=(setmap[x]**2+setmap[x])//2
        return count
    


nums=[1,2,3,1,1,3]
print(Solution().numIdenticalPairs(nums))