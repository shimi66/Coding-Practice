# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

from typing import List

'''
Initial thought
    - move from index -1,-1 all the way to 0,0 and figure out shortest path from each index

Final Thoughts
    - try to not use recursion/helper fuctions as they are expensive
    - precomputing the bottom row and right row prevents having to do bounds checks and does not increase 
    computation as long as the final loop ignores them
    - Otherwise I understood how to solve this problem and was able to implement a solution quickly.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for x in range(rows)]
        dp[-1][-1] = grid[-1][-1]

        for r in range(rows-2, -1, -1):
            dp[r][-1] = grid[r][-1] + dp[r+1][-1]

        for c in range(cols-2, -1, -1):
            dp[-1][c] = grid[-1][c] + dp[-1][c+1]

        for r in range(rows-2, -1, -1):
            for c in range(cols-2, -1, -1):
                dp[r][c] = min(grid[r][c] + dp[r+1][c], grid[r][c] + dp[r][c+1])

        return dp[0][0]
    
s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))