class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num%10!=0 or num==0
    
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. 
# Return true if reversed2 equals num. Otherwise return false.
