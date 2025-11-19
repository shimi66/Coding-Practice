# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

'''
Initial Thoughts
    - use conv to binary and check 1's/0's (1/2 min)
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        b = set(bin(n)[3:])
        return '1' not in b

        