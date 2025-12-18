# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

'''
Initial thoughts
    - add to a list and remove duplicates before appending
    - join list and return

    - concerns membership lookup in large list

Midway thoughts
    - struggling to understand lexicographical order

Final Thoughts
    - after misunderstanding the ordering, i struggled to go back to square one and rethink out a new
    solution that better fix the problem
    - after seeing how a stack was used for this question i could have definitely come up with this solution,
    though it didn't feel super optimized with storing the last occurance of each letter
    - i also had a misconception about greedy algorithms, thinking that the local decisions that were being made
    did not rely on other inputs and made the "best decision right now". for example if acb was in the stack, and the 
    full string was acbabc, when we saw acb a, we would keep the first a since cab is > abc. Instead a greedy 
    algorithm should greedily pick the prefix of our stack, based on if the other elements will appear later on.
    We would choose to remove acb from the stack and add the new a since we know that b and c will appear later 
    on in our input.
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        output = []

        for c in s[::-1]:
            if c in output:
                # this is going to take a lot of time
                add_new = [x for x in output if x != c]
                add_new.insert(0, c)
                output = min(add_new, output)
            else:
                output.insert(0, c)

        return "".join(output)
    

print(Solution().removeDuplicateLetters("abacb"))        

'''
bca
bca b
cab
bca

c
bc
abc
c abc
cab or abc = abc
b abc
bac or abc = abc

a
ab
ab a = ab
abc
abc b
'''

'''
Will try now that I understand what's going on, this doesn't feel like a greedy algorithm though
'''

class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}

        for i, c in enumerate(s):
            last_index[c] = i

        stck = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue 

            while stck and c < stck[-1] and i < last_index[stck[-1]]: 
                seen.remove(stck.pop())

            stck.append(c)
            seen.add(c)

        return ''.join(stck)
    
print(Solution2().removeDuplicateLetters("cbacdcbc"))        