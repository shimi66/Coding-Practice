# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

'''
Docstring for LeetCode.Easy.E_509
Initial thoguhts
    - create array of size n + 1
    - fill in array as we go
    - return last value
'''

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        arr = [0] * (n + 1)
        arr[1] = 1

        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[-1]

