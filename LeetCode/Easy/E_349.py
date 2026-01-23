# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) < len(nums2):
            return [n for n in nums1 if n in nums2]   
        else:
            return [n for n in nums2 if n in nums1] 