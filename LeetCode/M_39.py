# Given an array of distinct integers candidates and a target integer target, return a list of all unique 
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if 
# the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 
# 150 combinations for the given input.

from typing import List

'''
Initial Thoughts
    - First thought about factoring the number with the candidates
    - also thought about dropping all candidates greater than target
    - what if we started with the largest candidate 
        - how many times largest goes in, repeat with whats left
            - once we get to the end, one less than how many times

        - ie [2, 3, 5] and 8 ->
            - 5, 3
            - 3, 3, 2
            - 3, 2, 2 error
            - 2, 2, 2, 2
            - 2, 2, 2 error

        - would a stack be good for this? I think so
        - push elements on to the stack, when you pop off from the stack, we remove that number from available nums

Midway thoughts
    - popping from candidates started causing a nightmare, what if we just tracked which index we were on
    - reduces the need to copy lists during the recursion

Concluding thoughts
    - Changing from the popping of the candidates list to an index tracker was definitely the correct idea.
    - I should have realized that earlier since the pop on the candidates list made it harder to backtrack which
    was the whole point of practicing this problem
    - That said, using a stack was a great choice and really helped keep track of what our current "factorization" looked like
    - I cheated a little by having chatgpt quickly transition my code from a pop on the candidates to an index that was tracked
    though I could have implemented it on my own with some additional time.
    - Overall I was happy with how I thought about the problem, the data structures I used to implement it, and 
    the improvement I showed over my last backtracking problem.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted([x for x in candidates if x <= target], reverse=True)
        output = []
        stack = []

        def helper(idx: int, target):
            if target == 0:
                output.append(stack.copy())
                return
            if idx == len(candidates) or target < 0:
                return
            
            if candidates[idx] <= target:
                stack.append(candidates[idx])
                helper(idx, target - candidates[idx])
                stack.pop()

            helper(idx + 1, target)

        helper(0, target)
        return output
    
s = Solution()
print(s.combinationSum([2, 3, 5], 8))