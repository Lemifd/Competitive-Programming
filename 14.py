class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans=""
        for i in range(len(strs[0])):
            try:
                if all(strs[0][i]==c[i] for c in strs):
                    ans+=strs[0][i]
                    continue
                break
            except:
                break
            
        return ans
# strs = ["reflower","flow","flight"]
# strs=[""]
strs=["ab","a"]
print(Solution().longestCommonPrefix(strs))