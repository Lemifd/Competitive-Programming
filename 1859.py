class Solution:
    def sortSentence(self, s: str) -> str:
        #   return ' '.join([w[:-1] for w in sorted(s.split(), key=lambda x: x[-1])])

        a=s.split(" ")
        hashmap={}
        for i in a:
            hashmap[int(i[len(i)-1])]=i[:len(i)-1]
        print(hashmap)
        ans=""
        for i in range(1,len(hashmap)+1):
            if i!=len(hashmap):
               ans+=hashmap[i]+" "
            else:
                ans+=hashmap[i]
        return ans




s = "is2 sentence4 This1 a3"
print(Solution().sortSentence(s))