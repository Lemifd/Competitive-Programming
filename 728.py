class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        arr=[x for x in range(left,right+1) if '0' not in str(x)]
        return [x for x in arr if all(x%int(c)==0 for c in str(x))]

print(Solution().selfDividingNumbers(66,708))