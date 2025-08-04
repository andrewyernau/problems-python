#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

#You must write an algorithm that runs in O(n) time.
#Constraints:

#    0 <= nums.length <= 1000
#    -10^9 <= nums[i] <= 10^9


class Solution:
    
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        streak = 0
        for num in nums_set:
            if num -1 not in nums_set: # Check if it can continue a streak or not
                current_num = num
                new_sreak = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    new_sreak += 1
                streak = max(streak, new_sreak)
        return streak


nums = [2,20,4,10,3,4,5]
solution = Solution()
output = solution.longestConsecutive(nums)
print(f"Input: {nums}")
print(f"Output: {output}")  # Output: 4 (the longest consecutive sequence)