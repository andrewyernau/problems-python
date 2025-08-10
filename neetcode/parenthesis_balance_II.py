#Have the function BracketMatcher(str) take the str parameter being passed and 
# return 1 if the brackets are correctly matched and each one is accounted for.
# Otherwise return 0. For example: if str is "(hello (world))", then the output
# should be 1, but if str is "((hello (world))" the the output should be 0 because
# the brackets do not correctly match up. Only "(" and ")" will be used as brackets.
# If str contains no brackets return 1. 

class Solution:
    def BracketMatcher(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return 0
                stack.pop()

        return 1 if len(stack) == 0 else 0
    
input = "(c(oder)) b(yte)"
solution = Solution()
output = solution.BracketMatcher(input)
print("Input:", input)
print("Output:", output)  # Output: True