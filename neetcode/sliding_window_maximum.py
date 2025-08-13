#You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

#Return a list that contains the maximum element in the window at each step.

#Example 1:

#Input: nums = [1,2,1,0,4,2,6], k = 3

#Output: [2,2,4,4,6]

#Explanation: 
#Window position            Max
#---------------           -----
#[1  2  1] 0  4  2  6        2
# 1 [2  1  0] 4  2  6        2
# 1  2 [1  0  4] 2  6        4
# 1  2  1 [0  4  2] 6        4
# 1  2  1  0 [4  2  6]       6

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        slidingMaxs = []
        current_max = max(nums[0:k])
        slidingMaxs.append(current_max)
        for right in range(k, len(nums)):
            left = right - k + 1
            
            if nums[right] > current_max:
                current_max = nums[right]
            
            elif nums[left - 1] == current_max:
                current_max = max(nums[left:right+1])
            
            slidingMaxs.append(current_max)
        
        return slidingMaxs

solution = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
output = solution.maxSlidingWindow(nums,k)

print(f"Input: {nums},{k}")
print(f"Output: {output}") # Output : true