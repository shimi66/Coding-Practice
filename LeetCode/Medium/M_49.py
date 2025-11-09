# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
                
        return list(anagram_groups.values())
    
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
