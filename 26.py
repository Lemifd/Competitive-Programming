class Solution(object):
    def removeDuplicates(self, nums):
        ans=[]
        i=0
        while i<len(nums):
     
            try:
                if nums[i] in ans:
                    del nums[i]
                    continue
                else:
                    ans.append(nums[i])
                    i+=1
            except:
                pass
        return len(nums)

   
li=[0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(li))