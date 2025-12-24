# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# # Since the result may be very large, so you need to return a string instead of an integer.

from typing import List

'''
Initial Thoughts
    - sort by starting digits, make largest number, join all together?

Midway thoughts
    - mayber there is a better way.
    - while nums: pick largest starting dig, continue picking largest next dig until less than or equal to starting digit

    - my understanding of how this is a greedy problem is correct, however I am implementing it poorly
    - can i make this a recursive problem?

Final Thoughts
    - I understand how this was a greedy algorithm problem, but I stuggled to find the right algorithm in my head that would work
    - after readin gthe solution with the lexicographical sorting, it was very similar to what one of my later ideas was, but 
    implmented much cleaner and more efficient.
    - took 45+ min
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))

        # since max len of a number is 10 chars, we can have this custom sorting alg that makes use of lexicographical sorting to efficiently
        # order from largest to smallest while keeping the original values
        arr.sort(key=lambda x: x*10, reverse=True)

        if arr[0] == "0":
            return "0"
        
        return ''.join(arr)

print(Solution().largestNumber([0, 0]))