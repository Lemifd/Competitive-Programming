#done
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)<=1:
            return s

        for i in range(len(s)-1,-1,-1):
            s.append(s[i])
        del s[:len(s)//2]
        return s
        # s.reverse() alternative solution
        return s
    

s = ["h","e","l","l","o"]

print(Solution().reverseString(s))
