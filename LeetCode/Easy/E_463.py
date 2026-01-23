# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 
# represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by 
# water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

from typing import List
import heapq

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        perimeter = 0
        seen = set()
        queue = []
        heapq.heapify(queue)

        # find first island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # start here
                    heapq.heappush(queue, (r, c))
                    seen.add((r, c))
                    while queue:
                        curr_r, curr_c = heapq.heappop(queue)
                        for dr, dc in dirs:
                            new_r = curr_r + dr
                            new_c = curr_c + dc

                            if 0 <= new_r < rows and 0 <= new_c < cols:
                                if grid[new_r][new_c] == 0:
                                    perimeter += 1
                                else:
                                    if (new_r, new_c) not in seen:
                                        heapq.heappush(queue, (new_r, new_c))
                                        seen.add((new_r, new_c))
                            else:
                                perimeter += 1
                    return perimeter