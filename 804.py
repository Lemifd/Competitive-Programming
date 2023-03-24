class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans={}
        for i in range(len(words)):
            temp=""
            for s in words[i]:
                temp+=code[ord(s)-97]
            if temp not in ans:            
                ans[temp]=temp
    
        return len(ans)


words = ["gin","zen","gig","msg"]
print(Solution().uniqueMorseRepresentations(words))