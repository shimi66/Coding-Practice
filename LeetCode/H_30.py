# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all 
# concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from typing import List

'''
Initial thoughts 
    - window through s, and then window through the substring

Midway thoughts
    - passed 179 out of 182 until hit TLE
    - what if i sort words and then create a sorted list of the substring and just compare the lists?

Concluding thoughts
    - I cooked again
    - sorting and comparing the lists was definitely faster as it removed the second for loop in exchange for sorting a list of 
    size len(words). Also it is a much smaller amount of code. I pulled the sorting idea from one of the problems I did a couple 
    days ago where we were comparing chars in strings.

    - spent some time reading through the optimized hash map solution where they use a collections Counter and keep a running 
    dict of seen words. This allows to only look at strings of size len(words[0]) without having to recompute the whole substring and sort.
    I think I now understand how the sliding windows work and the parent offset for loop works to ensure all matches are garunteed to be 
    found in a much quicker manner.
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        window_size = word_size * len(words)
        output = []
        seen = []

        for i in range(len(s) - window_size + 1):
            substring = s[i:i+window_size]
            for j in range(len(words)):
                word = substring[j * word_size : j * word_size + word_size]
                if word in words:
                    seen.append(word)
                    words.pop(words.index(word))
                else:
                    break
            
            if len(words) == 0:
                output.append(i)
                words = seen
            else:
                words += seen
                
            seen = []
            
        return output
    
solution = Solution()
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))

class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        word_size = len(words[0])
        window_size = word_size * len(words)
        output = []

        for i in range(len(s) - window_size + 1):
            substring = s[i:i+window_size]
            sorted_list = sorted([(substring[j * word_size:j * word_size + word_size]) for j in range(len(words))])
            if sorted_list == words:
                output.append(i)

        return output
    
solution2 = Solution2()
print(solution2.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
    
