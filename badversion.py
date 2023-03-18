# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(self,n):
        if n >1702766718 :
            return True
        else:
            return False
    def firstBadVersion(self,n):
        beg=0 
        last=n 

        while(beg<last):
            mid=(beg+last)//2
            isit=self.isBadVersion(mid)
            if isit==True:
                if self.isBadVersion(mid-1)==False:
                   return mid
                else:
                    last=mid
            else:
                if self.isBadVersion(mid+1)==True:
                    return mid+1
                else:
                    beg=mid

        

# print(Solution().firstBadVersion(10))
print(Solution().firstBadVersion(2126753390))