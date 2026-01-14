# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted multiple times.

from typing import List

'''
Initial Thoughts
    - I stuggled to figure out a math trick to make this problem work and thought I was the issue so i looked at solutions
    - should have approached it from a coding perspective

    - define low and upper bounds, binary search on it until within tolerance

Final Thoughts
    - I get the premise of the problem but there really feels like there should be a cleaner solution so I didn't approach
    it from this way as it felt very brute force. There was a bunch of random math too.
'''

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        low, high = float('inf'), float('-inf')
        prev = float('inf')

        # find total area
        for [x, y, l] in squares:
            total_area += l*l
            low = min(low, y)
            high = max(high, y+l)


        for i in range(46):
            mid = (high-low)/2.0 + low

            if abs(prev - mid) < 0.00001:
                return mid
            else:
                prev = mid

            curr_area = 0.0

            for [x, y, l] in squares:
                if y > mid:
                    continue

                curr_area += l * max(0, min(mid - y, l))

            if curr_area >= total_area / 2.0:
                high = mid
            else:
                low = mid

        return mid

print(Solution().separateSquares([[0,0,2],[1,1,1]]))