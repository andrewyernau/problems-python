#Given a string s, return true if it is a palindrome, otherwise return false.

#A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.

#Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

class Solution:
    # Could be improved to O(1) space complexity, by not creating two lists and 
    # just using two pointers (increasing and decreasing)
    def isPalindrome(self, s: str) -> bool:
        left= []
        right = []
        for char in s:
            if len(left) > len(s)/2:
                break
            if char.isalnum():
                left.append(char.lower())
        for char in reversed(s):
            if len(right) > len(s)/2:
                break
            if char.isalnum():
                right.append(char.lower())
        if left == right:
            return True
            
        return False

s = "Was it a car or a cat I saw?"
solution = Solution()
is_palindrome = solution.isPalindrome(s)
print(f"Is the string a palindrome? {is_palindrome}")  # Output: True