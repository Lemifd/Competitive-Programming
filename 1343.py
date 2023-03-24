class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        val=threshold*k 
        R,sumv,ans=0,[0],0
        for i in range(len(arr)):
            sumv.append(arr[i]+sumv[-1])
            if i-R+1>k: 
                R+=1
            if i-R+1==k:
                if sumv[-1]-sumv[R]>=val:
                  ans+=1
        return ans
                
                



# arr = [2,2,2,2,5,5,5,8]
# k = 3
# threshold = 4
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3 
threshold = 5
print(Solution().numOfSubarrays(arr,k,threshold))