# You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on 
# the array any number of times:

# Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
# Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

# The gcd of two integers is the greatest common divisor of the two integers.

from typing import List
from collections import defaultdict
import math

'''
Initial Thoughts
    - two main issues we have
        - finding gcd of two elements
        - finding which elements to replace 
    - once you get one element to 1, you need n-1 more operations

    - I would guess this is a dp/backtracking problem...
    - could you factor each element, then compare factors amongst pairs, then select which one to replace?
        - this would be a greedy approach?
        - factor all elements
        - find which two elements have the gcd closest to one
            - if all elements have the same gcd, return -1

    - how to factor efficiently?
        - keep a dict of num to factors
        - only refactor when theres a new num in the array

Midway thoughts
    - the problem with below algorithm is in the selection of which pair of elements we should use
    - it picks the min of gcds but that is not always the best option.

    - I think that I am off track of what the solution should look like, however I think the way that I thought through this 
    problem was logical, used the factors hash map correctly, and only updated factors and gcds as needed: 47 min

    - read through the correct conceptual approach to this problem about finding gcd of sub arrays and will re-attempt below

    
Final Thoughts
    - I did not have the number theory part of this problem down off the top of my head (gcd of sub arrs = 1)
    - once that made sense to me, it was easy to implement a solution, though I was able to refine it into a much more efficeint
    version by incrementally building my gcds of sub arrays instead of recomputing it for a whole sub array at a time.

    - I didn't know about the math.gcd function either so that really helped once I learned of it. 
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def factor(num: int) -> set[int]:
            output = set([1, num])
            for i in range(1, math.floor(num**(0.5)) + 1):
                if num % i == 0:
                    output.add(i)
                    output.add(num//i)
            return output

        factors = defaultdict(set)
        operations = 0
        for num in nums:
            if not factors[num]:
                factors[num] = factor(num)

        gcds = [0] * (len(nums) - 1)
        changed_idx = -1
        while 1 not in nums:
            if changed_idx == -1:
                # compute all gcds
                for i in range(len(nums) - 1):
                    gcds[i] = max([x for x in factors[nums[i]] if x in factors[nums[i+1]]])
            else:
                # compute two affected gcds
                if changed_idx > 0:
                    gcds[changed_idx - 1] = max([x for x in factors[nums[changed_idx-1]] if x in factors[nums[changed_idx]]])
                if changed_idx < len(nums) - 1:
                    gcds[changed_idx] = max([x for x in factors[nums[changed_idx]] if x in factors[nums[changed_idx+1]]])

            if len(set(gcds)) == 1:
                return -1

            # # pick index smallest gcd from list
            gcd_index_to_pick = gcds.index(min(gcds))

            # pick largest of numbers from that gcd and its index
            if nums[gcd_index_to_pick] > nums[gcd_index_to_pick+1]:
                changed_idx = gcd_index_to_pick
            else:
                changed_idx = gcd_index_to_pick + 1

            # change it to gcd
            nums[changed_idx] = gcds[gcd_index_to_pick]
            operations += 1

            # factor if new number
            if not factors[nums[changed_idx]]:
                factors[nums[changed_idx]] = factor(nums[changed_idx])

        if 1 in nums:
            return len(nums) - nums.count(1) + operations
        return -1

# s = Solution()
# print(s.minOperations([4, 2, 6, 3]))

from functools import reduce

class Solution2:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if reduce(math.gcd, nums) != 1:
            return -1
        
        if nums.count(1) > 0:
            return n - nums.count(1)
        
        # start incrementally finding gcds
        min_subarr_len = float('inf')
        for i in range(n):
            gcd = nums[i]
            for j in range(i + 1, n):
                gcd = math.gcd(gcd, nums[j])
                if gcd == 1:
                    min_subarr_len = min(min_subarr_len, j - i + 1)


        return (min_subarr_len - 1) + (n - 1)
    
s2 = Solution2()
print(s2.minOperations([1, 2]))