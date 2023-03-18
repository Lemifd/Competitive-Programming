#done
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans=[]
        c=0
        for i in range(len(s)-2):
            ans.append(s[i:i+3])
        for i in ans:
            if len(i)==len(set(i)):
                c+=1
                print(f"{i} c={c}")

        return c


s = "aababcabc"
Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
print(Solution().countGoodSubstrings(s))