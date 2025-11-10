# You are given an array nums of size n, consisting of non-negative integers. 
# Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

# In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences 
# of the minimum non-negative integer in that subarray to 0.

# Return the minimum number of operations required to make all elements in the array 0.

from typing import List

'''
Initial Thoughts
    - similar to some other problem ive done
    - use a stack, when we find a num greater than whats on the stack, increase operations by 1
        - once at the end, add len of stack to operations
        ex [3, 1, 2, 1]
        - stack = [3, 1]
        - 2 > 1 so operations = 1
        - stack = [3, 1] so operations += 2
        ex [1, 2, 1, 2, 1, 2]
        - stack = [1]
        operations = 4 + len(stack)
        ex [1, 2, 4, 3, 3, 1]
        - I cant tell if this works but cant think of an immediate flaw so lets try it since it should be easy to implement

Midway Thoughts
        - doesnt work but we can do someting about it
        - im close but not quite correct on my algorithm

Concluding Thoughts
    - I was close but ultimately was messing up the logic in the algorithm. Monotonic stack made sense, but I think it is 
    generally hard for me to conceptually understand the logic on why the monotonic stack works or when we increment our 
    operations counter.
    - Need more practice
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        output = 0
        stack = []
        for num in nums:
            while stack and num < stack[-1]:
                stack.pop()
            if num > 0 and (len(stack) == 0 or num > stack[-1]):
                stack.append(num)
                output += 1

        return output
    
s = Solution()
print(s.minOperations([1, 2, 1, 2, 1, 2]))
    
