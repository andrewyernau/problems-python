class Solution:
    def hasDuplicate(nums: list[int]) -> bool:
        myset=set()

        for num in nums:
            if num in myset:
                return True
            myset.add(num)
        return False
    
run_test=(1,3,5,2)
print(Solution.hasDuplicate(run_test))