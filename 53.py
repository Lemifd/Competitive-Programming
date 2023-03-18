#done 2 way
class Solution:
    def maxsubarray(self,nums):
        # kadanes algoritms
        # maxSum=nums[0]
        # maxneg=[]
        # currSum=0
        # for i in nums:
        #     if i <0:
        #         maxneg.append(i)

        #     currSum=max(currSum+i,0)
        #     maxSum=max(currSum,maxSum)
        # if maxSum==0:
        #     return max(maxneg) if 0 not in nums else 0
        # return maxSum
       _MAX=-(10)**5
       curr=0
       for i in nums:
           curr+=i 
           if curr>_MAX:
               _MAX=curr
           if curr<0:
               curr=0
       return _MAX


n=[-2,1,-3,4,-1,2,1,-5,4]


print(Solution().maxsubarray(n))