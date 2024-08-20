class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:

        for i,value_i in enumerate(nums):
            for j, value_j in enumerate(nums):
                if i == j:
                    continue
                sum=value_i+value_j
                if sum==target:
                    return (i,j)

nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
target = 25
print(type(Solution.twoSum(nums,target)))