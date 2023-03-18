#done
class Solution:
    def mySqrt(self, x: int) -> int:
        #retun x**0.5
        left=0
        right=x+1
        while left<=right:
            if right-left==1:
                if right**2 > x:
                    return left
                else:
                    return right
            mid=(left+right)//2
            if x>mid**2:
                left=mid
            elif x<mid**2:
                right=mid
            else:
                return mid
