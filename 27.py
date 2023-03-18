class Solution:
    def removeElement(self, nums, val: int) -> int:
        # lis=[]
        # for i in range(len(nums)):
        #     if nums[i]==val:
        #         lis.append(i)
        # j=0
        # for i in lis:
        #     del nums[i+j]
        #     j-=1        
        # return len(nums)
        length = len(nums)
        i = 0
        while i<length:
            if nums[i] == val:
               del(nums[i])
               i -= 1
               length -=1
            i += 1
        return length



