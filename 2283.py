#done in 2ways
class Solution:
    def digitCount(self, num: str) -> bool:
        # hashmap={}
        # for i in num:
        #     if int(i) not in hashmap:
        #         hashmap[int(i)]=1
        #     else:
        #         hashmap[int(i)]+=1
        # for i in range(len(num)):
        #     if i not in hashmap:
        #         hashmap[i]=0
        # for i in range(len(num)):
        #     if int(num[i])!=hashmap[i]:
        #         return False
        # return True

        return all(num.count(str(i))==int(num[i]) for i in range(len(num)))

num = "1210"

print(Solution().digitCount(num))
         