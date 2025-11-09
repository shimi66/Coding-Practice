# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

from typing import List

'''
First thoughts
    - we can find the indicies of all zeros and record the rows/cols to be set to zero

Midway thoughts
    - this worked and passed all tests but doesn't use a hash map...
    - how would we use a hash map?

    - saw the additional follow up about devising a solution with O(1) space
    - will try in solution 2

Final thoughts
    - I struggled to come up with a O(1) solution. Using the first row/col as a marker while also using a constant
    space var to mark the first row/col was clever and something I think I have seen before but long ago. I could probably
    come up with this on my own in a new problem now that its fresh in my head but needed some assistance for this one.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        first_row_zero = any(i == 0 for i in matrix[0])
        first_col_zero = any(matrix[row][0] == 0 for row in range(num_rows))
        
        for row in range(1, num_rows):
            for col in range(1, num_cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for r in range(1, num_rows):
            for c in range(1, num_cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if first_col_zero:
            for row in range(num_rows):
                matrix[row][0] = 0
        if first_row_zero:
            for col in range(num_cols):
                matrix[0][col] = 0