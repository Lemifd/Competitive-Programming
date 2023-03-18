import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #bruteforce
        # if len(sentence)<26:
        #     return False
        # alphabets={x+1:index for x,index in enumerate(string.ascii_lowercase)}
        # for i in alphabets:
        #     if alphabets[i] not in sentence:
        #         return False
        # return True
        return True if len(set(sentence))==26 else False
    


        
       

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().checkIfPangram(sentence))