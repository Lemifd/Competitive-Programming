class Solution:
    def flipAndInvertImage(self, image):
        ans=[]
        for i in image:
            local=[]
            for j in range(len(i)-1,-1,-1):
                local.append(0 if i[j]==1 else 1)
            ans.append(local)
        return ans



    #     for i in range(len(image)):
    #         image[i]=self.revoin(image[i])
    #     return image
    # def revoin(self,nums):
    #     for i in range(len(nums)):
    #         if nums[i]==0:
    #             nums[i]=1
    #         else:
    #             nums[i]=0
    #     return [nums[x] for x in range(len(nums)-1,-1,-1)]
    
image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))