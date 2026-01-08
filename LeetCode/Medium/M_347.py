# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List
from collections import Counter
import heapq

'''
Initial Thoughts
    - use a counter to get "priority of each nums"
    - construct min heap with tuple (-count, num)
    - return top k elements from heap as a list with just the num

Final Thoughts
    - I cooked ngl
    - I remembered how to use heapq and collections well which brought my solution within the O(NlogN) time complexity
    that the additional requirement of the solution had (5 min)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        h = []
        output = []

        for num, count in counts.items():
            h.append((-count, num))
        
        heapq.heapify(h)

        while k:
            output.append(heapq.heappop(h)[1])
            k -= 1

        return output