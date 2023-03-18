class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(n)
        j=0
        for i in n:
            if int(i)==1:
                j+=1
        return j

print(Solution().hammingWeight(n))