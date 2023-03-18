class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        cond=True
        summ=0
        prod=1
        while n!=0:
 
            summ=summ + n%10
            prod=prod*(n%10)
            n=int(n/10)
        return prod-summ
            
print(Solution().subtractProductAndSum(234))