#Escribe una función que reciba una cadena con paréntesis y determine si están correctamente balanceados.

#Ejemplos:

#is_balanced("(())") => True
#is_balanced("(()") => False
#is_balanced(")()(") => False

class Solution:
    def is_balanced(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()

        return len(stack) == 0
    
input = "(())"
solution = Solution()
output = solution.is_balanced(input)
print("Input:", input)
print("Output:", output)  # Output: True