#Dado un string, comprímelo siguiendo esta lógica:

#Sustituye las repeticiones consecutivas de un carácter por el carácter 
# seguido del número de veces que aparece.

#Si la versión comprimida no es más corta que la original, devuelve el original.
#Ejemplo:

#compress("aabcccccaaa") => "a2b1c5a3"
#compress("abc") => "abc"

class Solution:
    def compress(self, s: str) -> str:
        compressed = []
        count = 1
        for i in range(1,len(s)):
           if s[i] == s[i-1]:
               count +=1
           else:
               compressed.append(s[i-1] + str(count))
               count = 1
        compressed.append(s[-1] + str(count))
        
        return "".join(compressed) if len("".join(compressed)) < len(s) else s

input = "aabcccccaaa"
solution = Solution()
output = solution.compress(input)
print("Input:", input)
print("Output:", output)  # Output: "a2b1c5a3"