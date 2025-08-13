#You are given an m x n 2-D integer array matrix and an integer target.

#    Each row in matrix is sorted in non-decreasing order.
#    The first integer of every row is greater than the last integer of the previous row.

#Return true if target exists within matrix or false otherwise.

#Can you write a solution that runs in O(log(m * n)) time?

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix[0])
        i = 0
        while i < len(matrix):
            #Vertical search
            if matrix[i][m-1] == target:
                return True
            elif target < matrix[i][m-1]:
                #Horizontal search
                left, right = 0, m -1
                while left <= right:
                    inner = (left + right) // 2
                    if matrix[i][inner] == target:
                        return True
                    elif matrix[i][inner] < target:
                        left = inner + 1
                    elif matrix[i][inner] > target:
                        right = inner - 1
            i+=1
        return False

solution = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
output = solution.searchMatrix(matrix,target)

print(f"Input: {matrix},{target}")
print(f"Output: {output}") # Output : true