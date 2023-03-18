class Solution:
    def countOdds(self, low: int, high: int) -> int:
    
      if low%2!=0:
        if (high-low+1)%2==0:
            return (high-low+1)/2
        else:
            return 1+(high-low+1)//2
      else:
         return (high-low+1)//2



print(Solution().countOdds(3,7))