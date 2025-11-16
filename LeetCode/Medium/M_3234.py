# You are given a binary string s.

# Return the number of substrings with dominant ones.

# A string has dominant ones if the number of ones in the string is greater than or 
# equal to the square of the number of zeros in the string.

'''
Initial Thoughts
    - seems like a dp or divide and conquer problem
    - brute force would be a sliding window
    - could compute counts and lens of sub strings

    - i feel like a sliding window that grows and shrinks is the correct way to approach this, but not sure how
    to move the window around

    - implementing brute force first

Midway thoughts
    - as i assumes, brute force hits TLE at 784/881 test cases (took 10 min)

    - could keep a dict of seen strings and if they are valid or not
    - only works for a little bit until memory gets too large

    - for each index, find all possible substrs starting from that index
        - increase window based on if a one or zero is seen
    - this is faster, we pass 844/881 but we still hit TLE (18 min)
    - we are doing too many wasted checks between indexes
    - we need to somehow dynamically change our count and window size when we encounter a new 1/0
    - could we keep a running counter of the +- 1's we have
        - if 0, we are -1 counter
        - if 1, we are +1
        - if 10 or 01 we are 0
        - if 110 we are +1
        - if 001 we are -3

    - prefix sums again huh, just creating a prefix_zeros array passes 855/881 until TLE

Concluding thoughts
    - giving up for now after 1 hr total on the problem
    - the optimization needed to pass the ridiculous test cases is wild

    - that being said, prefix sums and skipping window sizes base on num of zeros in substring is a solid idea
    - still need more practice with prefix sums
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        output = s.count('1')

        for window_size in range(2, len(s) + 1):
            for i in range(len(s) - window_size + 1):
                sub = s[i : i + window_size]
                num_zeros = sub.count('0')
                if num_zeros ** 2 <= window_size - num_zeros:
                    output += 1

        return output
    
s = Solution()
print(s.numberOfSubstrings("00011"))


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prefix_zeros = [0] * (n+1)
        output = 0

        for i, c in enumerate(s):
            prefix_zeros[i+1] = prefix_zeros[i] + (c == '0')

        def is_valid(b: int, e:int) -> bool:
            if s[b:e] == '':
                return False
            zeros = prefix_zeros[e] - prefix_zeros[b]
            return zeros**2 <= (e - b - zeros)

        j = 0
        for i in range(n):
            if j < i+1:
                j = i+1  
            while j < n and is_valid(i, j):
                j += 1
            output += j - i - 1

        return output
    
s2 = Solution2()
print(s2.numberOfSubstrings("00011"))