#You are given two strings s1 and s2.

#Return true if s2 contains a permutation of s1, or false otherwise. 
# That means if a permutation of s1 exists as a substring of s2, then return true.

#Both strings only contain lowercase letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        need = {}
        
        need_count = len(s1)
        
        for char in s1:
            need[char] = need.get(char,0) + 1
        # Once we know how which chars we need and how much of them
        # We can now iterate char by char if there is a permutation
        print(need)
        for i,char in enumerate(s2):
            have = {}
            subStr = s2[i:need_count+i]
            #Could be improoved in the future because I don't need 
            # to reset the whole window, just update the first and last element 
            # and keep the inner content untouched 
            # (reducing the time complexty from O(n*m) to just O(n))
            for subC in subStr:
                have[subC] = have.get(subC,0) + 1
            if need == have:
                return True
        return False

solution = Solution()
s1 = "abc"
s2 = "lecaabee"
output = solution.checkInclusion(s1,s2)

print(f"Input: {s1},{s2}")
print(f"Output: {output}") # Output : true