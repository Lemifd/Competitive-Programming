class Solution:
    def pivotInteger(self, n: int) -> int:
        a=sum([x for x in range(1,n+1)])
        b=0
        for i in range(1,n+1):
            b+=i
            if b==a-b+i:
                return i
        return -1

n=8
print(Solution().pivotInteger(n))