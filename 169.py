class Solution:
    def twoSum(self, numbers, target):

        for index, val in enumerate(numbers):
            if target - val in numbers[index+1:]:
                return [index+1,numbers[index+1:].index(target-val)+1+index+1]        
            

  

numbers=[2,7,8,10]
target=9

print(Solution().twoSum(numbers,target))