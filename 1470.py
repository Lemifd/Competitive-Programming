class Solution:
    def shuffle(self, nums, n: int):
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
            
        return ans
    



nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums,n))