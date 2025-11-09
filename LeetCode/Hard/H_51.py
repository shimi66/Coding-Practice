# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. 
# You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space, respectively.

from typing import List

'''
things we know
    - can be a max of 1 queen per row and col
    - num of queens in a valid solution = n

approaches:
    - place a queen in the top row
    - mark all un available spots with x
    - iterate through rows repeating this until you either place all queens or cant place a queen
    - repeat from beginning with queen in a new col

concerns with above approach:
    - TLE lol

midway thoughts:
    - what if i make a function that just places the first queen it can given a board with spaces that are unavailable
    - I could then make this recursive and see if it can place n queens or not

concluding thoughts:
    - I need to practice my backtracking problems more. After seeing the solution and stepping through how it works
    I found it more straight forward to implement. I think I could have implemented this without any help had I 
    had a stronger understanding of backtracking as in my first attempts, I had the right idea on how to solve
    the problem but couldn't implement the backtracking
'''
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [['.' for i in range(n)] for i in range(n)]

        def backtrack(row: int):
            # if we are at our end row we want to print out our board
            if row == n:
                output.append(["".join(board[row]) for row in range(n)]) 

            # for the row given, we will iterate through the colums and see if it safe to place a queen
            for col in range(0, n):
            # if it is
                if is_safe(row, col):
                    # place the queen
                    # backtrack on the next row
                    # remove the queen
                    # repeat
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

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
        
        backtrack(0)
        return output
    
solution = Solution()
print(solution.solveNQueens(4))

# class Solution2:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         board = [["." for _ in range(n)] for _ in range(n)]

#         def backtrack(row):
#             if row == n:
#                 res.append(["".join(r) for r in board])
#                 return
#             for col in range(n):
#                 if isSafe(row, col):
#                     board[row][col] = 'Q'
#                     backtrack(row + 1)
#                     board[row][col] = '.'

#         def isSafe(row, col):
#             for i in range(row):
#                 if board[i][col] == 'Q':
#                     return False
#             for i in range(1, min(row, col) + 1):
#                 if board[row - i][col - i] == 'Q':
#                     return False
#             for i in range(1, min(row, n - 1 - col) + 1):
#                 if board[row - i][col + i] == 'Q':
#                     return False
#             return True

#         backtrack(0)
#         return res
    
# solution2 = Solution2()
# print(solution2.solveNQueens(4))