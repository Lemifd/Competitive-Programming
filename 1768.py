#Done 2 way
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # ans=""
        # for i in range(max(len(word1),len(word2))):
        #     try:
        #         ans=ans+word1[i]
        #     except:
        #         ans=ans
        #     try:
        #         ans=ans+word2[i]
        #     except:
        #         ans=ans
        # return ans
        ans=""
        _min=min(len(word1),len(word2))
        for i in range(_min):
            ans=ans+word1[i]+word2[i]
        return ans+word1[_min+1:] if len(word1)>len(word2) else ans+word2[_min+1:]
        





word1 = "abc"
word2 = "pqr"
# Output: "apbqcr"

print(Solution().mergeAlternately(word1,word2))