#You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

#    Each row must contain the digits 1-9 without duplicates.
#    Each column must contain the digits 1-9 without duplicates.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

#Return true if the Sudoku board is valid, otherwise return false

#Note: A board does not need to be full or be solvable to be valid.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check rows
        for row in board:
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        #check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
                    
        #check 3x3 sub-boxes
        for row_box in range(3):
            for col_box in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row_box * 3 + i][col_box * 3 + j]
                        if num != '.':
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True
        
board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
solution = Solution()
is_valid = solution.isValidSudoku(board)
print(f"Is the Sudoku board valid? {is_valid}")  # Output: True