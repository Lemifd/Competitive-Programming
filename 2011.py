class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        hashmap= {"++X":1, "X++":1, "--X":-1, "X--":-1}
        x=0
        for i in operations:
            x+=hashmap[i]
        return x
        # x = 0
        # for o in operations:
        #     if "+" in o: 
        #         x += 1
        #     else:
        #         x -= 1
        # return x

