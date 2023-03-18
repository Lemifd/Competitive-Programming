#not done checkout


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet = {}
        ans = 0
        start = 0

        for index, letter in enumerate(s):

            if letter in alphabet:
                sums = alphabet[letter] + 1
                if sums > start:
                    start = sums
            num = index - start + 1

            if num > ans:
  
                ans = num

            alphabet[letter] = index

        return ans
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))