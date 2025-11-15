# Given an integer array nums, return true if any value appears at least twice in the array, and 
# return false if every element is distinct.

'''
Initial Thoughts
    - use counter (took 1min 30 sec to implement and is first 3 submissions)
    - could also use set (took 20 sec to implemnt and is next 3 submissions)

    - topics
        - sets/arrays
'''

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)