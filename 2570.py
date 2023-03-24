from collections import defaultdict
class Solution:
    def mergeArrays(self, nums1, nums2):
        # hashmap={}
        # new=sorted(nums1+nums2)
        # for i in new:
        #     if i[0] not in hashmap:
        #         hashmap[i[0]]=i[1]
        #     else:
        #         hashmap[i[0]]+=i[1]
        # return list(hashmap.items())
        C = defaultdict(int)
        for a,b in nums1:
            C[a]+=b
        for a,b in nums2:
            C[a]+=b
        
        return sorted([[a,C[a]] for a in C])
        
        
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(Solution().mergeArrays(nums1,nums2))