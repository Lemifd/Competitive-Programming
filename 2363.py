class Solution:
    def mergeSimilarItems(self, items1, items2):
        hasht={}
        new=sorted(items1+items2)
        for i in new:
            if i[0] not in hasht:
                hasht[i[0]]=i[1]
            else:
                hasht[i[0]]+=i[1]
        return [[x,hasht[x]] for x in hasht]



items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(Solution().mergeSimilarItems(items1,items2))
        