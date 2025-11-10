# There is a robot on an m x n grid. The robot is initially located at the top-left corner 
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to 
# reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

'''
Initial Thoguhts
    - we can keep a 2d matrix and each cell can record the number of unique paths exitst 
    from its current location.
    - work backwards from the bottom right corner to fill in all the cells until we reach
    the robot starting cell

Concluding Thoughts
    - This was definitely the right way to approach this problem and I am glad I was able to just slightly clean up 
    the code when I saw that I failed the m = 1, n = 1 case due to a poor choice along the way.
    - This is a bottom-up dynamic programming solution which increases the memory usage to O(nm) due to the 2d array
    however, this does not have the issue of running into maximum recursion depth (from a top-down solution) which I thought might happen for 
    larger inputs
    - That being said, I will also implement and solve the top-down dynamic programming with recursion for practice!
        - Now that I think about it, top down still needs O(nm) memory unless it wants to recompute a lot of stuff

        - The top down approach was pretty easy to implement after knowing the alogrithm used in the bottom up approach
        - Uses more memory since I still need to store the dp matrix, but now i need to allocate for the recursive function calls
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        dirs = [(1,0), (0,1)]
        
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if r == m - 1 and c == n - 1:
                    continue
                paths = 0
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        paths += dp[nr][nc]
                    
                dp[r][c] = paths

        return dp[0][0]

s = Solution()
print(s.uniquePaths(3, 7))

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        dirs = [(1, 0), (0, 1)]

        def helper(r: int, c: int) -> int:
            paths = 0
            if dp[r][c] != 0:
                return dp[r][c]
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    paths += helper(nr, nc)

            dp[r][c] = paths
            return paths
    
        return helper(0, 0)



s2 = Solution2()
print(s2.uniquePaths(23, 12))