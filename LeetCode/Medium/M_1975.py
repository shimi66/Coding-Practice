# You are given an n x n integer matrix. You can do the following operation any number of times:

# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.

# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of 
# the matrix's elements using the operation mentioned above.

from typing import List

'''
Initial Thoughts
    - Select the two numbers that when multiplied by -1, give the highest increase in total sum
    - repeat until no neg numbers or they will not increase total sum

    - how do we want to select the numbers
    - how do we want to store where the negative numbers are

    - dict of tuples?
    - must be an easier way but starting with this

Midway Thoughts
    - This can solve it but its really bad in larger matricies with lots of negative numbers
    - new thought approach
        - if a row has even neg numbers, we apply operations until theyre next to each other and cancel out
        - if a row has odd neg numbers, we can apply operations until theres only 1 neg number
            - then look to above and below rows to do it again
        - math formula for this based on num of neg numbers total?
        - at most, one negative number left
            - only if odd number of rows reduce to 1 neg number
        - 33 min

Final Thoughts
    - I came to a clever solution that is fast and constant memory, however I did not touch much on the fact that this was a 
    greedy problem.
    - I think I know what the greedy approach is (seen in my initial thoughts), but I did not solve it this way as it 
    seemed too complicated and inefficient.
'''

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num_neg = 0
        total = 0
        min = 10 ** 5
        for row in matrix:
            for col in row:
                total += abs(col)
                if col < 0:
                    num_neg += 1
                if abs(col) < min:
                    min = abs(col)

        if num_neg % 2 == 0:
            return total
        
        return total - (2 * min)


print(Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))
