#You are given an integer array heights where heights[i] represents the height of the ithith bar.

#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            # Get inner area of the bucket
            width = right - left
            height = min(heights[left],heights[right])
            area = width * height
            max_area = max(max_area, area)
            # Move the pointer of the smallest height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
    
height = [1,7,2,5,4,7,3,6]
solution = Solution()
output = solution.maxArea(height)
print(f"Input: {height}")
print(f"Output: {output}")  # Output: 36