class Solution:
    def countPoints(self, rings: str):
        hashmap={}
        c=0
        for i in range(1,len(rings),2):
            if rings[i] not in hashmap:
                hashmap[rings[i]]=rings[i-1]
            else:
                if rings[i-1] not in hashmap[rings[i]]:
                    hashmap[rings[i]]+=rings[i-1]
        for key, val in hashmap.items():
            if len(val)==3:
                c+=1
        return c


rings = "B0B6G0R6R0R6G9"

print(Solution().countPoints(rings))