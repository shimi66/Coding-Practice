# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

from typing import List

'''
Initial thoughts
    - binary search on last col, the binary search on row]

Final thoughts
    - been awhile since ive written a binary search. also felt weird doing it on a col of a 2d matrix but it 
    made sense in the end
    - it was good to learn more about bisect and what it does. could have used it twice if there was an easy
    way to extract the last col of the matrix into a 1d array but not in log n time.
    - was good practice and I think I could do this again quicker with and without the bisect library
'''

import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0]) 

        # find row
        start = 0
        end = rows-1
        while start < end:
            mid = (end + start) // 2
            if matrix[mid][-1] < target:
                start = mid + 1
            else:
                end = mid

        found_idx = bisect.bisect_left(matrix[start], target)
        return found_idx < cols and matrix[start][found_idx] == target
        
s = Solution()
print(s.searchMatrix([[-9,-8,-8],[-5,-3,-2],[0,2,2],[4,6,8]], 15))