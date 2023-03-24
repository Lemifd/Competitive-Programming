#done 2way
class Solution:
    def sortPeople(self, names, heights):
        # bruteforce
        # sort={}
        # for i in range(len(names)):
        #     sort[heights[i]]=names[i]
        # ans=[]
        # for i in range(len(sort)):
        #     try:
        #         ans.append(sort[max(sort)])
        #         del sort[max(sort)]
        #     except:
        #         pass
        # return ans
        _2D=[]
        for i in range(len(names)):
            _2D.append([heights[i],names[i]])
        sort_2D=sorted(_2D,reverse=True)
        return [sort_2D[i][1] for i in range(len(sort_2D))]





names = ["Mary","John","Emma"]
heights = [180,165,170]
print(Solution().sortPeople(names,heights))