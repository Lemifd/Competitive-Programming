from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashmap=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            a=sum([int(x) for x in str(i)])
            hashmap[a]+=1
        return max([x for x in hashmap.values()])
    

lowLimit = 1
highLimit = 10

print(Solution().countBalls(lowLimit,highLimit))