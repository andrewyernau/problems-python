#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

#Each product is guaranteed to fit in a 32-bit integer.

#Follow-up: Could you solve it in O(n)O(n) time without using the division operation?
import math

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = []
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            solution.append(left[i] * right[i])
        return solution
    
nums = [1,2,4,6]
solution = Solution()
output = solution.productExceptSelf(nums)
print(f"Input: {nums}")
print(f"Output: {output}") #Output: [48,24,12,8]