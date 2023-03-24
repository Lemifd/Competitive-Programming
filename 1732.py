#prefix sum
class Solution:
    def largestAltitude(self, gain) -> int:
        _sum=0
        _max=0
        for i in range(len(gain)):
            _sum+=gain[i]
            if _sum>_max:
                _max=_sum
        return _max