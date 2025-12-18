# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only 
# constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically 
# contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
# tonight without alerting the police.

from typing import List

'''
Initial thoughts
    - return max of (rob 1 and rob(nums[2:]), dont rob 1 and rob(nums[1:]))
    - store max of index range for reuse

Midway thoughts
    - TLE at 48/70. likely due to how many times we recreate nums.
    - change to an index solution

Final thoughts
    - I COOKED 15 min or so
    - Lots of interuptions but overall I came up with the solution and its optimization pretty quick
    - implementing it wasn't too bad as I had a pretty solid understanding of how to break this problem down into
    subproblems.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {} # key = starting index, value = max of rob(nums[i:])
        n = len(nums)

        def helper(start_idx: int):
            if start_idx >= len(nums):
                dp[start_idx] = 0
                return
            if start_idx == len(nums) - 1:
                dp[start_idx] = nums[-1]
                return
            
            if start_idx in dp:
                return dp[start_idx]
            else:
                helper(start_idx + 2)
                helper(start_idx + 1)
                dp[start_idx] = max(nums[start_idx] + dp[start_idx + 2], dp[start_idx + 1])

        helper(0)
        
        return dp[0]
        
        
print(Solution().rob([2,7,9,3,1]))