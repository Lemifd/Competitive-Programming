class Solution:
    def kthDistinct(self, arr, k: int) -> str:
        hashmap={}
        for i in arr:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        c=1
        for key,val in hashmap.items():
            if val==1:
                if c==k:
                    return key
                else:
                    c+=1
        return ""
        
arr = ["d","b","c","b","c","a"]
k = 2
print(Solution().kthDistinct(arr,k))

# distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
#  If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.