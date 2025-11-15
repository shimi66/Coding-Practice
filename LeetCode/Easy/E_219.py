# Given an integer array nums and an integer k, return true if there are two distinct indices 
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

'''
Initial Thoughts
    - Sliding window of k
    - check set on that window 17 min

    - lots of edge cases to check
'''

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len == 1 we cannot have distinct i and j
        if len(nums) == 1:
            return False
        
        # if len nums is smaller than k then we set the whole array
        if len(nums) <= k:
            return len(set(nums)) != len(nums)

        # compute sets over the sliding window and check its length
        s = set(nums[0:k+1])
        if len(s) != k + 1:
            return True
        for i in range(0, len(nums) - k - 1):
            s.remove(nums[i])
            s.add(nums[i+k+1])
            if len(s) != k + 1:
                return True
        return False


        