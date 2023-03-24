class Solution:
  def reverse(self, x: int) -> int:
    if x<0:
        x=-1*x
        return -1*int(str(x)[::-1]) if -1*int(str(x)[::-1]) in range(-2**31,2**31) else 0
    elif x>0 and x%10!=0:
        return int(str(x)[::-1]) if int(str(x)[::-1]) in range(-2**31,2**31) else 0
    else:
        while x%10!=0:
            x=x//10
        return int(str(x)[::-1]) if int(str(x)[::-1]) in range(-2**31,2**31) else 0
    #   if x <-2**31 or x>2**31-1:return 0
    # return int(str(x)[::-1]) if x>0 else -1*int(str(-1*x)[::-1]) if x<0 else 0


