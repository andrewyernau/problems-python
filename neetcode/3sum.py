#Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
# and the indices i, j and k are all distinct.

#The output should not contain any duplicate triplets. 
# You may return the output and the triplets in any order.

#Explanation:
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            #avoid duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
        return result
            

nums = [-1,0,1,2,-1,-4]
solution = Solution()
output = solution.threeSum(nums)
print(f"Input: {nums}")
print(f"Output: {output}")  # Output: [[-1,-1,2],[-1,0,1]]