#done
class Solution:
    def maxArea(self, height) -> int:
        L=0
        R=len(height)-1
        _maxA=0
        while L<=R:
            _maxA=max(_maxA,min(height[L],height[R])*(R-L))
            if height[L]>height[R]:
                R-=1
            else:
                L+=1
            
        return _maxA



height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(Solution().maxArea(height))
