# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         rem=""
#         for letter in s:
#             if letter.islower:
#                 if letter.upper() not in s[::]:
#                    rem=rem+letter
#             else:
#                 if letter.lower() not in s[::]:
#                     rem =rem+letter
#         return T
            



# s = "YazaAay"
# # Output: "aAa

# print(Solution().longestNiceSubstring(s))