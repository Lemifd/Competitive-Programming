class Solution:
    def numberOfMatches(self, n: int) -> int:
        # matches=0
        # while True:
        #     if n%2==0:
        #         matches+=n//2
        #         n/=2
        #     else:
        #         matches+=n//2
        #         n=1+(n-1)/2

        #     if n==1:
        #         return int(matches)
        return n-1


n = 7
print(Solution().numberOfMatches(n))