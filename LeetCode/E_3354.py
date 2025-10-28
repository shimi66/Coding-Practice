# You are given an integer array nums.

# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement 
# direction of either left or right.

# After that, you repeat the following process:

# If curr is out of the range [0, n - 1], this process ends.
# If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, 
# or decrementing curr if you are moving left.
# Else if nums[curr] > 0:
# Decrement nums[curr] by 1.
# Reverse your movement direction (left becomes right and vice versa).
# Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid if 
# every element in nums becomes 0 by the end of the process.

# Return the number of possible valid selections.


'''
Initial thoughts 
    - you are looking for what indexes make the two sublists equal

Concluding thoughts
    - need to review prefix sums a little more and how they can be used to improve time complexity
    - correct way of thinking about the problem as well as solution
'''
from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        output = 0
        for i, num in enumerate(nums):
            if num == 0:
                # check left direction start balance
                if 0 <= sum(nums[:i]) - sum(nums[i:]) <= 1:
                    output += 1
                # check right direction start balance
                if 0 <= sum(nums[i+1:]) - sum(nums[:i+1]) <= 1:
                    output += 1
        return output

solution = Solution()
print(solution.countValidSelections([16,13,10,0,0,0,10,6,7,8,7]))

class Solution2:
    def countValidSelections(self, nums: List[int]) -> int:
        output = 0
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        total_sum = prefix[-1]

        for i, num in enumerate(nums):
            if num == 0:
                # check left direction start balance
                if 0 <= prefix[i] - (total_sum - prefix[i]) <= 1:
                    output += 1
                # check right direction start balance
                if 0 <= (total_sum - prefix[i+1]) - prefix[i+1] <= 1:
                    output += 1
        return output
    