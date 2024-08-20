class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_dict = {i: None for i in range(len(nums))} ###we create a map where the key means the times (by using idexes) a number is reapeated and the value is a list of these numbers
        print(number_dict)
        


nums = [1,2,2,2,2,3,3]
k = 2
solution = Solution()
sol=solution.topKFrequent(nums,k)
print("Solution is ",sol)