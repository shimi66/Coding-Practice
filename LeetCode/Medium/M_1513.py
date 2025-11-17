# Given a binary string s, return the number of substrings with all characters 1's. 
# Since the answer may be too large, return it modulo 109 + 7.

'''
Initial thoughts
    - one pass through s, track 1's block size

Concluding thoughts
    - I had the right approach but it could be optimized into the solution below. It was embarassing how long
    it took me to remember the n(n+1)/2 formula (i kept doing n(n-1)/2). This feels like it should be an
    easy level problem
'''

class Solution:
    def numSub(self, s: str) -> int:
        output = 0

        ones_length = 0

        for c in s:
            if c == '1':
                ones_length += 1
                output += ones_length
            else:
                ones_length = 0

        return output % (10**9 + 7)
    
s = Solution()
print(s.numSub("0110111"))

import time
import random

# ------------------------
# Your original algorithm
# ------------------------
class SolutionOriginal:
    def numSub(self, s: str) -> int:
        output = 0

        one_start = s.find('1')
        in_zeros = False

        for i in range(one_start, len(s)):
            if s[i] == '1':
                if in_zeros:
                    one_start = i
                    in_zeros = False
                continue
            else:
                if in_zeros:
                    continue
                else:
                    in_zeros = True
                    n = i - one_start
                    output += int((n * (n+1)) / 2)
        
        if s[-1] == '1':
            n = len(s) - one_start
            output += int((n * (n+1)) / 2)

        return output % (10**9 + 7)


# ------------------------
# Optimized incremental count
# ------------------------
class SolutionOptimized:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        current = 0

        for c in s:
            if c == '1':
                current += 1
                count += current
            else:
                current = 0
        
        return count % MOD


# ------------------------
# Benchmark function
# ------------------------
def benchmark(s):
    sol_orig = SolutionOriginal()
    sol_opt = SolutionOptimized()

    print("Length of test string:", len(s))

    t1 = time.time()
    sol_orig.numSub(s)
    t2 = time.time()

    t3 = time.time()
    sol_opt.numSub(s)
    t4 = time.time()

    print(f"Original time:   {t2 - t1:.6f} seconds")
    print(f"Optimized time:  {t4 - t3:.6f} seconds")


# ------------------------
# Create test strings
# ------------------------

# All ones (worst/biggest stretch)
s1 = "1" * 500_000

# Random binary string
s2 = "".join(random.choice("01") for _ in range(500_000))

print("\n--- Benchmark: All Ones ---")
benchmark(s1)

print("\n--- Benchmark: Random String ---")
benchmark(s2)
