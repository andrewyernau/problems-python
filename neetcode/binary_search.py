#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

#Your solution must run in O(logn)O(logn) time.

#Example 1:

#Input: nums = [-1,0,2,4,6,8], target = 4

#Output: 3

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            inner = (left + right) // 2
            
            if nums[inner] == target:
                return inner
            elif nums[inner] < target:
                left = inner + 1
            elif nums[inner] > target:
                right = inner - 1
        return -1

solution = Solution()
nums = [-1,0,2,4,6,8]
target = 4
output = solution.search(nums,target)

print(f"Input: {nums},{target}")
print(f"Output: {output}") # Output : 3