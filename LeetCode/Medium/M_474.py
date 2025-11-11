# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.

from typing import List
from collections import Counter

'''
Initial Thoughts
    - Can i just use counter on each str and then a comparison?
    - misunderstood the problem
    - m and n are max in the output set not per string

    - do max form on sub arrays?
    - every time we include an element, reduce m and n, call recursively with different list
    - can we use index ptrs instead of copying the list
    - for every element, we can include or not include
        - if we include, we subtract m and n and recall on further list
        - if we dont include, remove from list and recall

Midway thoughts
    - TLE exceeded at 25/77 test cases. Not surprised as I can see repeat calcs being done
    - how can i store the max for each sub string list 

    - let me try with some dp now
    - problem is that i lose track of 0s and 1s counter with the dict

Concluding thoughts
    - I was correct that dp was the right way to approach this problem, but I struggled to find the pattern which
    would allow me to make use of a DP algorithm.
    - After reading and walking through a DP implmentation of this knapsack problem, I was able to reason my way though
    the implmentation. 
    - I continue to understand dp but the hardest part for me is recognizing the subproblem which overlaps and I could
    take advantage of.
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        max_subset_len = 0
        subset = []
        # zeros and ones == 0
        def helper(string_list: List[str], zeros_left: int, ones_left: int) -> int:
            nonlocal max_subset_len, subset
            if zeros_left < 0 or ones_left < 0:
                return -1
            if len(string_list) == 0 or (zeros_left == 0 and ones_left == 0):
                return len(subset)
            

            counts = Counter(string_list[0])
            tmp = string_list.pop(0)
            dont_include = helper(string_list, zeros_left, ones_left)
            subset.append(tmp)
            include = helper(string_list, zeros_left - counts['0'], ones_left - counts['1'])
            subset.pop(-1)
            string_list.append(tmp)
                
            return max(include, dont_include, max_subset_len)
        
        return helper(strs, m, n)
    
s = Solution()
print(s.findMaxForm(["10","0001","111001","1","0"], 4, 3))

class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros

            for z in reversed(range(zeros, m + 1)):
                for o in reversed(range(ones, n + 1)):
                    dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)

        return dp[-1][-1]

s2 = Solution2()
print(s2.findMaxForm(["10","0001","111001","1","0"], 4, 3))
