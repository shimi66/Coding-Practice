# Given a string s, partition s such that every substring of the partition is a palindrome. 
# Return all possible palindrome partitioning of s.

from typing import List
from math import ceil

'''
Initial thoughts
    - all elements by themselves are palindromes
    - search for all palindromes
    - for distinct palindromes we can include them both

    - think from dp perspective
        - part(abcd) = all palindromes including a + part(bcd)

Midway thoughts
    - i think i have the basis down and I am just complicating the implementation 37 min
    - part(abcd) = dp[a] + dp[bcd]
    - if not known
        - dp[bcd] = dp[b] + dp[cd] + all palindromes > len 1 starting with b
        - dp[cd] = dp[c] + dp[d] + is cd a a palindrome
        - dp[d] = [['d']]
        - dp[cd] = [['c', 'd']] 

    - part(aab) = dp[a] + dp[ab] + (all plindromes len > 1 starting from i = 0 + leftovers)
    - dp[a] = [['a']]
    - dp[ab] = dp['a'] + dp['b'] + is ab a palindrome
    - dp['b'] = [['b']]
    - dp['ab'] = [['a', 'b']]
    - dp['aab'] = [['a', 'a', 'b'], ['aa', dp['b']]]
    - dp['aab'] = [['a', 'a', 'b'], ['aa', 'b']]
    
    - part(aaba) = dp[a] + dp[aba] + (all plindromes len > 1 starting from i = 0 + leftovers)
    - dp[a] = [['a']]
    - dp[aba] = dp['a'] + dp['ba'] + (all plindromes len > 1 starting from i = 0 + leftovers)
    - dp[ba] = dp[b] + dp[a] + is ba a palindrome
    - dp[b] = [[b]]
    - dp[ba] = [[b, a]]
    - dp[aba] = [[a, b, a], [aba]]
    - dp[aaba] = [[a, a, b, a], [a, aba]]
    - dp[aaba] = [[a, a, b, a], [a, aba], [aa, b, a]]

    - stopping here but logic wise i understand the solution. i just struggled with a clean implementation 56 min
'''

from collections import defaultdict

class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if not s:
            return []
        if n == 1:
            return [[s]]
        
        dp = defaultdict(list)
        
        output = set()

        def find_palindromes_with_first_c(input: str) -> List[str]:
            o = []
            for j in range(1, m+1):
                sub = input[0:j]
                if sub == sub[::-1]:
                    o.append(sub)
            return o
        
        def helper(input: str):
            if dp[input]:
                return dp[input]
            m = len(input)
            if m == 1:
                dp[input] = [[input]]

            first_part = dp[input[0:1]]
                

        for i in range(1, n+1):
            first_char_palindromes = find_palindromes_with_first_c(s[0:i])
            first_part = self.helper(s[0:i])
            second_part = self.helper(s[i:n+1])
            print()
            # combine parts


        return output
    

class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans