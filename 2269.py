#done
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        L,R,c=0,k-1,0
        if len(str(num))==1:
           return 1

        while R<len(str(num)):
         try:
            if num%int(str(num)[L:R+1])==0:
                c+=1
                print(str(num)[L:R+1])
         except:
            pass
         L+=1
         R+=1
        
        return c






num = 11
k = 1
# Output: 2

print(Solution().divisorSubstrings(num,k))