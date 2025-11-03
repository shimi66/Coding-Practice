# You are given two integers m and n representing a 0-indexed m x n grid. 
# You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] 
# represent the positions of the ith guard and jth wall respectively.

# A guard can see every cell in the four cardinal directions (north, east, south, or west) 
# starting from their position unless obstructed by a wall or another guard. A cell is guarded 
# if there is at least one guard that can see it.

# Return the number of unoccupied cells that are not guarded.

from typing import List

'''
Initial Thoughts
    - shouldnt be to hard to come up with a solution thats O(m^2 * n^2) 
    - ie brute force

    - cant think of a way to simplify this

    - read the hint and i guess thats what I was going to do anyways so here goes

Midway thoughts
    - this solution hits TLE at 40/49 test cases which I kind of expected
    - maybe add a hashmap that can reduce wasted stuff?

Concluding thoughts
    - well it definitely sped it up but this was such a bad solution.

    - actually the solution was correct however I could have been saving time by placing all of the guards
    before checking their vision so i didnt have to recheck the when blocked by another guard
'''

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0 for i in range(n)] for i in range(m)]

        def vision_checker(pos_x: int, pos_y:int, x_offset:int, y_offset:int):
            pos_x += x_offset
            pos_y += y_offset
            while 0 <= pos_x <= m-1 and 0 <= pos_y <= n-1 and board[pos_x][pos_y] < 2:
                board[pos_x][pos_y] = 1
                pos_x += x_offset
                pos_y += y_offset

        for r, c in walls:
            board[r][c] = 2

        for r, c in guards:
            board[r][c] = 2
        
        for r, c in guards:
            vision_checker(r, c, 1,0)
            vision_checker(r, c, -1,0)
            vision_checker(r, c, 0,1)
            vision_checker(r, c, 0,-1)

        return sum(cell == 0 for row in board for cell in row)
    
s = Solution()
print(s.countUnguarded(1, 5, [[0,1],[0,2],[0,3]], [[0,0]]))