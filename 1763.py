class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        for letter in s:
            if letter.islower:
                if letter.upper() not in s[::]:
                    return False
            else:
                if letter.lower() not in s[::]:
                    return False
        return True
            



s = "YazaAay"
# Output: "aAa

print(Solution().longestNiceSubstring(s))