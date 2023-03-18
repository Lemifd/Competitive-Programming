class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return "false"
        elif x==0:
            return "true"
        else:

            a=str(x)
            b=[]
            for i in a:
                b.append(i)
            c=[]
            c=c+b 
            b.reverse()
            print(b)
            print(c)
            if b==c:
                return "true"
            else:
                return "false"

print(Solution().isPalindrome(1212))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(0))
            