class Solution:
    def sumOfUnique(self, nums) -> int:
        hasht={}
        add=0
        for i in nums:
            if i not in hasht:
                hasht[i]=1
            else:
                hasht[i]+=1
        for i,j in hasht.items():
            if j==1:
                add+=i
        return add

nums =[10,4,10,9,5]
print(Solution().sumOfUnique(nums))