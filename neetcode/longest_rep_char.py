#You are given a string s consisting of only uppercase english characters 
# and an integer k. You can choose up to k characters of the string and 
# replace them with any other uppercase English character.

#After performing at most k replacements, return the length of the longest 
# substring which contains only one distinct character.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) > 1000 or len(s) < 1 or k < 0 or k > len(s):
            return 0
        
        count = {}  # Frecuencia de cada caracter en la ventana
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])  # Actualizamos el más frecuente
            
            # Si necesitamos más de k reemplazos, movemos la ventana
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

solution = Solution()
s = "AAABABB"
k = 1
output = solution.characterReplacement(s,k)

print(f"Input: {s},{k}")
print(f"Output: {output}") # Output : 4