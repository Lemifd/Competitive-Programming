#done
class Solution:
    def searchRange(self, nums, target):
       class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
           a=nums.index(target)
        except:
            return [-1,-1]
        ans=[a]
        for i in range(a+1,len(nums)):
            if target==nums[i]:
                ans.append(i)
            else:
                break 
        if len(ans)==1:
            ans.append(ans[0])
        else:
            ans=[min(ans),max(ans)]
        return ans if len(ans)>0 else [-1,-1]