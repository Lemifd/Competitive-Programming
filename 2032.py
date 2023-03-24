#done in 3way
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        #  hasht={}
        # for i in set(nums1):
        #     if i not in hasht:
        #         hasht[i]=1
        # for i in set(nums2):
        #     if i not in hasht:
        #         hasht[i]=1
        #     else:
        #         hasht[i]+=1
        # for i in set(nums3):
        #     if i not in hasht:
        #         hasht[i]=1
        #     else:
        #         hasht[i]+=1
        # ans=[]
        # for i in hasht:
        #     if hasht[i]>1:
        #         ans.append(i)
        # return ans
        #@ approach
        n1_set, n2_set, n3_set = set(nums1), set(nums2), set(nums3)
        res = set()
        for num in nums1:
            if num in n2_set or num in n3_set:
                res.add(num)
        for num in n2_set:
            if num in n1_set or num in n3_set:
                res.add(num)
        return list(res)
        # n_1,n_2,n_3=set(nums1),set(nums2),set(nums3)
        # n_12=set.intersection(n_1,n_2)
        # n_13=set.intersection(n_1,n_3)
        # n_23=set.intersection(n_2,n_3)
        # return list(set(list(n_12)+list(n_23)+list(n_13)))
        
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(Solution().twoOutOfThree(nums1,nums2,nums3))