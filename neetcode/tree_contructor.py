#Have the function TreeConstructor(strArr) take the array of strings stored in strArr,
# which will contain pairs of integers in the following format: (i1,i2), 
# where i1 represents a child node in a tree and the second integer i2 signifies that
# it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], 
# then this forms the following tree: 

# 4 - 2 = 1 7

class Solution:
    def TreeConstructor(self, strArr: list[str]) -> bool:
        if strArr is None:
            return False
            
        parentMap = dict()
        childrenCount = dict()
        
        for pair in strArr:
            pair_clean = pair[1:-1]
            i1_str, i2_str = pair_clean.split(",")
            i1, i2 = int(i1_str), int(i2_str)
            
            if i1 in parentMap:
                if parentMap[i1] != i2:
                    return False
            else:
                parentMap[i1] = i2
                childrenCount[i2] = childrenCount.get(i2,0)+1
                if childrenCount[i2] > 2:
                    return False
                
        return True
        
        

s = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
sol=Solution()
output = sol.TreeConstructor(s)
print(f"Input {s}")
print(f"Output {output}")
