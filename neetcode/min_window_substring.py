#Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, 
# which will contain only two strings, the first parameter being the string N and the 
# second parameter being a string K of some characters, and your goal is to determine 
# the smallest substring of N that contains all the characters in K. For example: if s
# trArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the 
# characters a, e, and d is "dae" located at the end of the string. So for this example 
# your program should return the string dae.

#Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring 
# of N that contains all of the characters in K is "aabd" which is located at the 
# beginning of the string. Both parameters will be strings ranging in length from 1 to 
# 50 characters and all of K's characters will exist somewhere in the string N. 
# Both strings will only contains lowercase alphabetic characters. 

class Solution:
    def minWindowSubstring(self, strArr):
        mainStr = strArr[0]
        goalStr = strArr[1]

        need = {}
        
        #Get the chars we need and the amount
        for c in goalStr:
            need[c] = need.get(c, 0) + 1
            
        have = {}
        have_count = 0
        need_count = len(need)  # number of distinct characters we need

        #Begin with the worst case, no result with the complete window
        res = ""
        min_len = len(mainStr) + 1
        
        #Now we initialize the loop to check by char if it is needed, if yes, -1 the need amount
        left = 0
        for right in range(len(mainStr)):
            #We can start from righ to left adding all letters we have in the given order
            c = mainStr[right]
            have[c] = have.get(c, 0) + 1

            # Do we have the same amount than we need for that char? If yes, + 1
            if c in need and have[c] == need[c]:
                have_count += 1

            # We made sure we have at least all we need, now find the shortest result
            while have_count == need_count: # This is true or then the result will be empty
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    res = mainStr[left:right+1]
                
                # Reduce left side
                left_char = mainStr[left]
                have[left_char] -= 1

                # cannot make it smaller from the left
                if left_char in need and have[left_char] < need[left_char]:
                    have_count -= 1

                left += 1

        return res

input = ["ahffaksfajeeubsne", "jefaa"]
solution = Solution()
output = solution.minWindowSubstring(input)
print("Input:", input)
print("Output:", output)  # Output: aksfaje