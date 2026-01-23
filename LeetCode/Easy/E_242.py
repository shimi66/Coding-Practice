# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

'''
Docstring for LeetCode.Easy.E_242
Initial thoughts
    - create a counter for both and compare? 2 min for this solution

Midway thoughts
    - how can we make it more memory efficient? ( 1 more min )
        - sort both and compare?
        - O(nlogn) to sort each
        - space is O(n + m)

    - remove letters from one string? (6.5 min to implement)
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)

        for key, val in s_counter.items():
            if t_counter[key] != val:
                return False
            
        return True
    
print(Solution().isAnagram('rat', 'car'))