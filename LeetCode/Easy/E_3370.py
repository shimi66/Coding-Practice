# You are given a positive number n.

# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)[2:]
        if '0' in binary:
            return 2 ** (len(binary)) - 1
        return n
    
