#You are given an array of non-negative integers height which represent an elevation map. 

# Each value height[i] represents the height of a bar, which has a width of 1

#Return the maximum area of water that can be trapped between the bars.

class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[:i])
            right_max = max(height[i + 1:])
            water = min(left_max, right_max) - height[i]
            if water > 0:
                total += water
        return total
                
            
height = [0,2,0,3,1,0,1,3,2,1]
solution = Solution()
output = solution.trap(height)
print(f"Input: {height}")
print(f"Output: {output}")  # Output: 9

height =[0,1,0,2,1,0,1,3,2,1,2,1]
output = solution.trap(height)
print(f"Input: {height}")
print(f"Output: {output}")