class Solution:
    def search(self, nums, target: int) -> bool:
        #return i in nums
        a=nums[nums.index(min(nums)):]
        b=nums[:nums.index(min(nums))]
        if target <=a[-1] and target>=a[0]:
            return self.binary(a,target)
        elif target <=b[-1] and target>=b[0]:
            return self.binary(b,target)
        else:
            return False
        

    
    def binary(self, num, target):
        if len(num)==1:
            if target==num[0]:
                return True
            else:
                return False
        left=0
        right=len(num)-1
        while left<right:
            if right-left==1:
                if target in [num[left],num[right]]:
                    return True
                else:
                   return False
            mid=(left+right)//2
            if target>num[mid]:
                left=mid
            elif target <num[mid]:
                right=mid
            else:
                return True
    


nums=[2,2,2,3,2,2,2]
target = 3

print(Solution().search(nums,target))