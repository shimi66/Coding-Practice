# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

from typing import List

'''
Initial thoughts 
    - bfs/dfs on a one to explore the island
    - keep track of unvisited nodes (ones)

Midway thoughts
    - TLE at 48/49 test cases
    - Solution works but how can we speed it up
        - well making the "unvisited_ones" into a set speeds it up enough to pass all tests

    - There might be a clever way to do this problem, but I think I implemented the goal solution. Using BFS/DFS to explore the 
    islands, and count how many there are.
    - I used a stack and implmented a BFS but it could have been done with a queue/DFS.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        stck = []
        islands = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        unvisited_ones = set([(i, j) 
                            for i in range(num_rows) 
                            for j in range(num_cols) 
                            if grid[i][j] == "1"])
        
        while unvisited_ones:
            stck.append(unvisited_ones.pop())
            islands += 1
            while stck:
                curr_x, curr_y = stck.pop(0)
                for dx, dy in dirs:
                    nx = curr_x + dx
                    ny = curr_y + dy
                    if 0 <= nx < num_rows and 0 <= ny < num_cols:
                        if (nx, ny) in unvisited_ones:
                            stck.append((nx, ny))
                            unvisited_ones.remove((nx, ny))

        return islands
    
s = Solution()
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

'''
More optimized solution below
    - using collections deque
    - using the grid to mark my "seen" ones instead of my "unvisited_ones" array

    - pop() pops from end of array making it behave like a stack
    - popleft() pops from the front making it behave like a queue
        - this is faster when we are appending things as well due to not having to fight about appends/pops
        - happening in different locations
'''

from collections import deque

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        q = deque()
        num_rows = len(grid)
        num_cols = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for x in range(num_rows):
            for y in range(num_cols):
                if grid[x][y] == "1":
                    q.append((x, y))
                    grid[x][y] = "0"
                    islands += 1
                    while q:
                        curr_x, curr_y = q.popleft()
                        for dx, dy in dirs:
                            nx = curr_x + dx
                            ny = curr_y + dy
                            if 0 <= nx < num_rows and 0 <= ny < num_cols:
                                if grid[nx][ny] == "1":
                                    q.append((nx, ny))
                                    grid[nx][ny] = "0"

        return islands
    
s2 = Solution2()
print(s2.numIslands([["1","0","1"],["0","1","0"],["1","0","1"]]))