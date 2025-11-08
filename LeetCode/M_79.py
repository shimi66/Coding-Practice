# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

from typing import List

'''
Initial Thoughts
    - DFS based on letters in word with a seen array of indicies so we don't revisit them
    - use a stack to implement
    - can recurse given that we pass our seen array in?

Concluding thoughts
    - I got to the right answer and used the right data structure, but included a lot of unecessary overhead
    that really hurt my execution time.
    - Arrays are really slow to work with as well as recursion that has lots of object creation. If I can use 
    my variables in place, it will be faster and more memory efficient.
    - It was a good practice for DFS but I need to keep working on it.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def helper(row: int, col: int, idx: int, seen: List) -> bool:
            if len(word) == 0 or idx == len(word):
                return True
            
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in seen or
                board[row][col] != word[idx]
            ):
                return False
            
            seen.add((row, col))

            for dx, dy in directions:
                if helper(row + dx, col + dy, idx + 1, seen):
                    return True
                    
            seen.remove((row, col))
            return False
                
        for row in range(rows):
            for col in range(cols):
                if helper(row, col, 0, set()):
                    return True

        return False
    
s = Solution()
print(s.exist([["A"]], "A"))