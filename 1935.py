class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr=text.split()
        c=0
        for i in arr:
            if len(set(i).intersection(set(brokenLetters)))==0:
               c+=1
        return c 





text = "hello world"
brokenLetters = "ad"
print(Solution().canBeTypedWords(text,brokenLetters))

# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters 
# of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.