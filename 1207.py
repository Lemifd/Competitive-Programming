from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hasht={}
        for i in arr:
            if i in hasht:
                hasht[i]+=1
            else:
                hasht[i]=1
        return True if len(hasht)==len(Counter(hasht.values())) else False
    

                