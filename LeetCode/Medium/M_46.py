# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

from typing import List
import time

'''
Initial Thoughts
    - use back tracking where we pick one number, permute the rest recursively
    - pick another number, permute the rest recursively

    - concerns about how many recursive calls

Final Thoughts
    - Took 10 min with 0ms runtime.
    - I was concerned about the runtime with how manyt calls were possible with larger and larger inputs
    but thankfully the input length was limited to 6. I tried running it all the way up to an input of length
    10 which took about 17 seconds to run.
    - I am glad that I recognized the backtracking pattern as it is not my strongest problems but I understood
    the concept of permutations very strongly so it made it easier to conceptualize that I could recursively 
    call permute, but that i had to add the num back in after each time so we could permute starting with
    another number.
    - Overall this was a great performance :)
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        if not nums:
            return output
        if len(nums) == 1:
            return [nums]
        
        copy = nums.copy()
        
        for num in copy:
            nums.remove(num)
            perms = self.permute(nums)
            for perm in perms:
                output.append([num] + perm)
            nums.insert(0, num)

        return output
        
start_time = time.time()
print(Solution().permute([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("time taken: " + str(time.time() - start_time))
