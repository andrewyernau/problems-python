#Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.

#Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

#You should aim for a solution with O(m) time for each encode() and decode()
# call and O(m+n) space, where m is the sum of lengths of all the strings and
# n is the number of strings. 

class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        if len(strs) >= 100: # Constraint 0<= strs.length < 100
            return ""
        for s in strs:
            if len(s) >= 200:
                return "" # Constraint 0 <= strs[i].length < 200
            encoded_string += f"{len(s)}#{s}"
        return encoded_string
        
    def decode(self, s: str) -> list[str]:
        decoded_strings = []
        separator = '#'
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded_strings.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded_strings

# Example usage
encode_text = ["hello", "world", "this", "is", "a", "test"]
solution = Solution()
encoded = solution.encode(encode_text)
print(f"Encoded: {encoded}")

decode_text = "5#hello5#worl#d4#this2#is1#a4#test"
decoded = solution.decode(decode_text)
print(f"Decoded: {decoded}")