# You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat 
# filled with zeroes.

# You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the 
# following operation:

# Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner 
# (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
# Return the matrix mat after performing every query.

from typing import List

'''
Initial Thoughts
    - we have to traverse all the queries at least once, question is, is there a way to speed up the incrementing of 
    the submatricies?
    - concerned about TLE and runtime

    - hashmap the indicies for fast increments?

Midway thoughts
    - solution works but TLE at n = 387 and lots of queries 10 min

    - how could we precompute the subarry increments

    - read and understand prefix sums more, store the cumulative increments in a diff matrix so its constant time over the queries
    - then a final pass of n to reconstruct the final array
    - i will now attempt it below 

Final Thoughts
    - I could understand I needed to sum the rectangles faster, but I did not have a strong enough understanding
    of prefix sums to implement the solution without some additional help. I think it would have been easier
    if it was a prefix sums problem on 1d arrays since I wouldn't have had to deal with the issue of double
    counting certain sums but I have a much better understaning of the principle behind the algorithm/approach
    now than before I started. I still need some practice with it though
'''

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        hashmap = {(r,c): 0 for r in range(n)
                            for c in range(n)}
        
        for query in queries:
            sr = query[0]
            sc = query[1]
            er = query[2]
            ec = query[3]
            for r in range(sr, er + 1):
                for c in range(sc, ec + 1):
                    hashmap[(r,c)] += 1
        output = [[0 for _ in range(n)] for _ in range(n)]
        for key, val in hashmap.items():
            output[key[0]][key[1]] = val
        return output
    
s = Solution()
print(s.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))

class Solution2:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n+1) for i in range(n+1)]
        output = [[0] * (n+1) for i in range(n+1)]

        for sr, sc, er, ec in queries:
            # encode rectangle
            diff[sr][sc] += 1
            diff[sr][ec + 1] -= 1
            diff[er + 1][sc] -= 1
            diff[er + 1][ec + 1] += 1

        for r in range(n):
            for c in range(n):
                # compute prefix sums here
                output[r][c] = diff[r][c] + output[r-1][c] + output[r][c-1] - output[r-1][c-1]

        output = output[:-1]
        output = [row[:-1] for row in output]
        return output

s2 = Solution2()
print(s2.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]]))