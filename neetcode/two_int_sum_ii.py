#Given an array of integers numbers that is sorted in non-decreasing order.

#Return the indices (1-indexed) of two numbers, [index1, index2], 
# such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

#There will always be exactly one valid solution.

#Your solution must use O(1)O(1) additional space.

#Explanation:
#The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        solution = []
        while left < right:
            temp_sum = numbers[left ] + numbers[right]
            if temp_sum == target:
                solution.append(left + 1)
                solution.append(right + 1)
                return solution
            elif temp_sum < target:
                left += 1
            else:
                right -= 1
        return solution

numbers = [1,2,3,4]
target = 3
solution = Solution()
output = solution.twoSum(numbers, target)
print(f"Input: {numbers}, Target: {target}")
print(f"Output: {output}")  # Output: [1, 2]