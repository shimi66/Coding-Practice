# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving 
# the order of characters. No two characters may map to the same character, but a character may map to itself.

'''
Docstring for LeetCode.Easy.E_205
Initial Thoughts
    - hashmap where we can encode letters to positions
    - compare two hashmaps
'''

from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}

        s_ctr = 0
        t_ctr = 0
        for i in range(len(s)):
            if s[i] not in s_hash:
                s_hash[s[i]] = s_ctr
                s_ctr += 1
            if t[i] not in t_hash:
                t_hash[t[i]] = t_ctr
                t_ctr += 1

            if s_hash[s[i]] != t_hash[t[i]]:
                return False
            
        return True

    
print(Solution().isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"))