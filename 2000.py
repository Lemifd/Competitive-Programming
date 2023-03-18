#done two way
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
           ind=word.index(ch)
           return word[ind::-1]+word[ind+1:]
        except:
           return word
        # ans=""
        # start=False
        # if ch not in word:
        #    return word
        # for i in range(len(word)):
        #     if start:
        #      ans=ans+word[i]
        #      continue
        #     ans=word[i]+ans
        #     if word[i]==ch:
        #        start=True
        # return ans
            



word = "abcdef"
ch = "d"
#dcbaefd
print(Solution().reversePrefix(word,ch))