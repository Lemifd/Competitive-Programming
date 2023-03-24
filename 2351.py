class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hasht={}
        for i in range(len(s)):
            if s[i] not in hasht:
                hasht[s[i]]=i
            else:
                return s[i]
s = "abccbaacz"

print(Solution().repeatedCharacter(s))