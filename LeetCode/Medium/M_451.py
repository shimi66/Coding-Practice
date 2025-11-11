# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

'''
Initial thoughts
    - can you use counter on a string?
    - if not we can create a dict, sort based on value (num times it shows up)
    - and then just build the string

Midway thoughts
    - well that worked and was a clean solution. How can I do this with a priority queue/heap

    - take 2
'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s).most_common()
        output = ''
        for key, val in counts:
            output += key * val
        return output
    
s = Solution()
print(s.frequencySort('reett'))

import heapq

'''
this is sorting alphabetical not by count...

this next solution feels dumb because its just a more complicated above but...
'''

class Solution2:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        output = ''
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (-1 * val, key))
        
        while heap:
            freq, ltr = heapq.heappop(heap)
            output += ltr * (freq * -1)
        return output
    

s2 = Solution2()
print(s2.frequencySort('reett'))