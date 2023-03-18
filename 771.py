class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        hashtable=set()
        for i in jewels:
            hashtable.add(i)
        for j in stones:
            if j in hashtable:
                count+=1
        return count