#Given a string s, find the length of the longest substring without duplicate characters.

#A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        
        max_len = 0 #Max length only can be the different chars
        left = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len

solution = Solution()
input = "pwwkew"
output = solution.lengthOfLongestSubstring(input)

print(f"Input: {input}")
print(f"Output: {output}") # Output : 3