class Solution:
    def fib(self, n: int) -> int:
        # if n==0 or n==1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        
        return 0 if n==0 else 1 if n==1 else self.fib(n-1) + self.fib(n-2)

print(Solution().fib(n=8))