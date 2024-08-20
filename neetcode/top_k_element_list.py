class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_dict = {}
        for value in nums:
            if value in number_dict:
                getcount = number_dict[value]
                getcount += 1
                number_dict[value] = getcount
            else:
                number_dict[value] = 1
        print(number_dict)
        sorted_orginial_dict=sorted(number_dict.items(), key = lambda x:x[1], reverse = True)
        print(sorted_orginial_dict)
        filtered_dict= [sorted_orginial_dict[i] for i in range(k)]
        return_list=[i[0] for i in filtered_dict]
        return return_list


nums = [1,2,2,2,2,3,3]
k = 2
solution = Solution()
sol=solution.topKFrequent(nums,k)
print("Solution is ",sol)