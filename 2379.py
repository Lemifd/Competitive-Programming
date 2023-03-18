class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=0
        for i in range(len(blocks)-5):
            if blocks[i]=="W" or i==0 and blocks[i+k+1]=="W":
                for j in range(i+1,i+k+1):
                    if blocks[j]=="W":
                        c+=1
        return c


     

blocks = "WBBWWBBWBW"
k = 7
# Output: 3

print(Solution().minimumRecolors(blocks,k))