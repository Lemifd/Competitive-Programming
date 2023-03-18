#done
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        #bruteforce
        # ans=[]
        # for i in range(len(nums)):
        #     counter=0
            
        #     for k in nums:
        #         if k<nums[i]:
        #            counter+=1
        #     ans.append(counter)

        # return ans
        copy=sorted(nums)
        hasht={}
        for i,j in enumerate(copy):
            if j not in hasht:
                hasht[j]=i
        return [hasht[i] for i in nums]
        



nums=[8,1,2,2,3]
print(Solution().smallerNumbersThanCurrent(nums))