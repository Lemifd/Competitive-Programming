#done
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        
        for i in range(len(matrix)):
            if self.binary(matrix[i],target):
                return True
        return False

    

    def binary(self,nums,target):
        left=0
        right=len(nums)-1
        if len(nums)==1:
            if target==nums[0]:
                return True
            else:
                return False
        while left<=right:
            if right-left==1:
                if target in [nums[right],nums[left]]:
                    return True
                else :
                    return False
            
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid
            elif target<nums[mid]:
                right=mid
            else:
                return True
            

matrix = [[1]]
target = 0
print(Solution().searchMatrix(matrix,target))                



        