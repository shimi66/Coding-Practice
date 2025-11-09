# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no 
# two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

class Solution:

    def totalNQueens(self, n: int) -> int:
        output = 0
        board = [['.' for i in range(n)] for i in range(n)]

        def backtrack(row: int, out: int) -> int:
            # if we are at our end row we want to print out our board
            if row == n:
                out += 1

            # for the row given, we will iterate through the colums and see if it safe to place a queen
            for col in range(0, n):
            # if it is
                if is_safe(row, col):
                    # place the queen
                    # backtrack on the next row
                    # remove the queen
                    # repeat
                    board[row][col] = 'Q'
                    out = backtrack(row + 1, out)
                    board[row][col] = '.'
            return out

        # safe check
        # does not need to check same row
        def is_safe(row: int, col: int) -> bool:
            # check col
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # check diag left
            for i in range(1, min(row, col) + 1):
                if board[row - i][col - i] == 'Q':
                    return False
            # check diag right
            for i in range(1, min(row, n - 1 - col) + 1):
                if board[row - i][col + i] == 'Q':
                    return False
            return True
        
        output = backtrack(0, output)
        return output
    
solution = Solution()
print(solution.totalNQueens(4))