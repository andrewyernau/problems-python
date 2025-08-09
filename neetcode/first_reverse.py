#Have the function FirstReverse(str) take the str parameter 
# being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" 
# then your program should return the string sredoC dna dlroW olleH.
class Solution:
    def FirstReverse(self, strParam:str) -> str:

        # code goes here
        sol = ""
        for i in range(len(strParam) - 1, -1, -1):
            sol += strParam[i]
        return sol

# keep this function call here 

solution = Solution()
input = "coderbyte"
output = solution.FirstReverse(input)
print(f"Input: {input}")
print(f"Output: {output}")