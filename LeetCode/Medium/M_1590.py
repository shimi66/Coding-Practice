# Given an array of positive integers nums, remove the smallest subarray (possibly empty) 
# such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.

from typing import List

'''
Initial Thoughts
    - sub array = continuous
    - compute modulo of sum and p
    - find smallest sub array who's sum is equal to px + modulo

    - since the subarry has to be continuous, we can use a prefix sum to compute these checks quickly

    - brute forcing the check on what the shortest sub arry feels like its inefficient

Midway thoughts
    - so brute forcing the check with window size was definitely too inefficient
    - tle at 135/145

    - use prefix sums to compute a hashmap where we store the value of what remainder is located
    - at an earlier index

Final thoughts
    - I was close with my use of prefix sums and calculating the remainder but I needed to take it one step
    further and store the remainders i had wish i had seen previously to solve the shortest subarr

    - This was a really goo problem to practice both prefix sums and hash maps.
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        pref_sum = 0
        total_remainder = sum(nums) % p
        remainder_locations = {0: -1}
        output = n

        if total_remainder == 0:
            return 0
        
        for i, num in enumerate(nums):
            # The remainder of the sum of everything I’ve seen so far.
            pref_sum = (pref_sum + num) % p
            # If I end the subarray here, what prefix remainder would I have needed earlier so 
            # that the removed chunk fixes the divisibility problem?
            target = (pref_sum - total_remainder) % p

            if target in remainder_locations:
                output = min(output, i - remainder_locations[target])

            remainder_locations[pref_sum] = i

        
        return output if output < n else -1
        

print(Solution().minSubarray([17,3,16,12,3,19,1,8,5,8], 54))