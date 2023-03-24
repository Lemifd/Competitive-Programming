class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        count=0
        for i in words:
            if len(set(i).difference(set(allowed)))==0:
                count+=1
        return count
    

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(Solution().countConsistentStrings(allowed,words))        
