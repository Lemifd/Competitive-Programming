class Solution:
    def sortedSquares(self, nums):
        sqr=[]
        for i in nums:
            sqr.append(i*i)
    
        def merge(lis):
            if len(lis)<=1:
                return lis
            mid=len(lis)//2
            left=lis[:mid]
            right=lis[mid:]
            left=merge(left)
            right=merge(right)
            print(f"left={left}")
            print(f"right={right}")
         
            return list(sorted(left,right))
        def sorted(left,right):
            ans=[]
            
            while len(left)!=0 and len(right)!=0:
                if left[0]<right[0]:
                    ans.append(left[0])
                    left.remove(left[0])
                else:
                    ans.append(right[0])
                    right.remove(right[0])
                if len(left)==0 or len(right)==0:
                    
                    return  ans+left+right
        merge(sqr)
nu=[ 2,1,3, 4, 5]
print(Solution().sortedSquares(nu))
# nums = [-4,-1,0,3,10]
# print(Solution().sortedSquares(nums))