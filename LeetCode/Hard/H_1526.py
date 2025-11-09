# You are given an integer array target. You have an integer array initial of the same size as target 
# with all elements initially zeros.

# In one operation you can choose any subarray from initial and increment each value by one.

# Return the minimum number of operations to form a target array from initial.

# The test cases are generated so that the answer fits in a 32-bit integer.


'''
Initial thoughts
    - do a greedy recursive approach
        - find longest subarray of non 0's
        - subtract 1 from subarray indexes
        - add one to output
        - repeat until target is all 0's 

Midway through thoughts
    - working solution but TLE after 50 cases which I anticipated after seeing the runtime of the algorithm I was writing. How can I reduce
    the wasted amount of compute...?
    - I see that stack is listed under the topics of the problem so how could i implement this with a stack...?
    - hint was about decrementing a range by the rang minimum which is definitely interesting
        - what if I split the array where there are 0's and repeat that above strategy?

Midway thoughts pt 2:
    - working solution again but memory exceed at test 127/129. 
    - I think this was a decent attempt and I will review solutions now.


Concluding thoughts
    - Read the theory behind an O(N) time complexity and O(1) space complexity solution and it is interesting and I am 
    still trying to wrap my head around why it works
    - Definitely an intersting and intuitive way of solving it by looking at the differences between the numbers

    - I vaguely see how a stack/monotonic stack is being used here but its more the concept of it over everything else
'''

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # return two ints in an array, first in is the index, second int is the length
        def longest_nonzero_subarr(input: List[int]) -> List[int]:
            longest_index = 0
            longest_length = 0
            curr = 0
            length = 0
            for idx, num in enumerate(input):
                if num == 0:
                    curr = idx + 1
                    length = 0
                else:
                    length += 1
                    if length > longest_length:
                        longest_index = curr
                        longest_length = length

            return [longest_index, longest_length]

        output = 0
        # for now we will use sum as a way to check if we are done
        while sum(target) > 0:
            # find longest subarray of non zero values
            subarr = longest_nonzero_subarr(target)
            target[subarr[0]:subarr[0] + subarr[1]] = [x - 1 for x in target[subarr[0]:subarr[0] + subarr[1]]]
            output += 1
        
        return output
    
solution = Solution()
print(solution.minNumberOperations([3,1,5,4,2]))

class Solution2:
    def minNumberOperations(self, target: List[int]) -> int:
        if len(target) == 0:
            return 0
        if len(target) == 1:
            return target[0]

        output = 0
        non_zero_subs = []
        tmp = []
        for num in target:
            if num == 0:
                if len(tmp) > 0:
                    non_zero_subs.append(tmp)
                    tmp = []
            else:
                tmp.append(num)
        
        if len(tmp) > 0:
            non_zero_subs.append(tmp)

        for subarr in non_zero_subs:
            subarr_min = min(subarr)
            subarr = [x - subarr_min for x in subarr]
            output += subarr_min
            output += self.minNumberOperations(subarr)

        return output
    
solution2 = Solution2()
print(solution2.minNumberOperations([3,1,5,4,2]))

class Solution3:
    def minNumberOperations(self, target: List[int]) -> int:
        output = target[0]

        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                output += target[i] - target[i-1]

        return output

solution3 = Solution3()
print(solution3.minNumberOperations([3,1,5,4,2]))