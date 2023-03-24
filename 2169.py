class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        _max,_min=max(num1,num2),min(num1,num2)
        c=0
        while num1>0 and num2>0:
            num1,num2=max(num1,num2),min(num1,num2)
            num1-=num2
            c+=1
        return c
    
        # count = 0
        # while(num1 and num2):
        #     if(num1 >= num2):
        #         count += (num1 // num2)
        #         num1 = num1 % num2
        #     else:
        #         count += (num2 // num1)
        #         num2 = num2 % num1
        # return count

print(Solution().countOperations(1,0))