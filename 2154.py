class Solution:
    def findFinalValue(self, nums, original: int) -> int:
        # if original in nums:
        #     return self.findFinalValue(nums,2*original)
        # else:
        #     return original
        stop = False
        while stop == False:
            if original in nums:
                original *= 2
            else:
                stop = True
        return original
    

    

