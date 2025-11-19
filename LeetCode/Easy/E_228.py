# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer 
# x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

'''
Initial Thoughts
    - single pass, keep track of start/end of consecutive nums (15 min, hard to debug)
'''

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        output = []

        s = 0
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                o = str(nums[s])
                if i > s + 1:
                    o += "->" + str(nums[i-1])
                
                output.append(o)
                s = i

        if s < n:
            o = str(nums[s])
            if n > s + 1:
                o += "->" + str(nums[n-1])
                
            output.append(o)
            
        return output
        