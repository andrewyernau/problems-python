#Dado un string con palabras separadas por espacios, ordénalas de menor a mayor longitud.
# Si dos tienen la misma longitud, mantén el orden original.

#Ejemplo:

#sort_by_length("la nave espacial despega ya") => "la ya nave despega espacial"

class Solution:
    def sort_by_length(self, s: str) -> str:
        words_split= s.split(" ")    
        words_split.sort(key=lambda x: len(x))
        words_split = " ".join(words_split)
        return words_split
    
input = "la nave espacial despega ya"
solution = Solution()
output = solution.sort_by_length(input)
print("Input:", input)
print("Output:", output)