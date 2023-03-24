class Solution:
    def destCity(self, paths) -> str:
        # hashmap=dict(paths)
        # start=paths[0][0]
        # while True:
        #     if start not in hashmap:
        #         return start
        #     start=hashmap[start]
        source=[x for x,y in paths]
        destination=[y for x,y in paths ]
        for city in destination:
            if city not in source:
                return city
        







# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().destCity(paths))