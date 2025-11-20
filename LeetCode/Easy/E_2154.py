# You are given an array of integers nums. You are also given an integer original which is the 
# first number that needs to be searched for in nums.

# You then do the following steps:

# If original is found in nums, multiply it by two (i.e., set original = 2 * original).
# Otherwise, stop the process.
# Repeat this process with the new number as long as you keep finding the number.
# Return the final value of original.

from typing import List

'''
Initial thoughts
    - first will implement brute force and then look for better solutions (1 min to read and implement)
        - used a set to speed up the "in" check

Final Thoughts
    - this was definitely the best approach given I dont have memory constraints. If i did, i would be concerned about
    nums itself. It is faster and easier to read/implement
'''

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums:
            original *= 2
        return original