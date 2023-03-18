#done
class Solution:
    def reverseWords(self, s: str,ss="") -> str:
        if " " in s:
            ind=s.index(" ")
            word=s[:ind]
            for i in range(len(word)-1,-1,-1):
                ss=ss+word[i]
            ss=ss+" "
            return self.reverseWords(s[ind+1:],ss)
                
        else:
             for i in range(len(s)-1,-1,-1):
                ss=ss+s[i]
        return ss



s = "Let's take LeetCode contest"
word=s[:s.index(" ")]
print(f"help {len(word)}")
print(Solution().reverseWords(s))
        