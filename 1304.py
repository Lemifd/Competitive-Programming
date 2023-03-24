class Solution:
    def sumZero(self, n: int):
        if n%2==0:
            return [x for x in range(-n//2,1+n//2,1) if x!=0]
        else:
            return [x for x in range(-1*(n//2),1+n//2,1)]
        # sol = []
        # for i in range(1,n):
        #     sol.append(i)
        # sol.append(-sum(sol))
        # return sol

n=1
print(Solution().sumZero(n))
