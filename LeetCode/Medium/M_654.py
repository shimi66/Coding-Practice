# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

'''
Initial thoughts
    - select max
    - split tree based on indexes
    - perform same operation for left/right subtree

Midway thoughts
    - The fact I implmented that in one shot with no logic errors is kind of wild ( 12 min )
    - Runs slow which I didn't expect since i tried doing this with list index pointers and not copying any lists
        - maybe due to finding the largest num and its index?
    - will try to improve runtime

    - read an interesting approach about using stacks to make this a single pass algorithm 
        - will try to implement with no help below

Final thoughts
    - I was able to implement the stack solution after drawing out an example and understanding the premise behind
    the approach
    - I think I would need more practice with these problems before I would come up with that solution approach, but
    the implementation was not the issue.
'''

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        largest = max(nums)
        largest_i = nums.index(largest)
        root = TreeNode(largest)

        # right_i is non inclusive
        def helper(left_i: int, right_i: int) -> Optional[TreeNode]:
            nonlocal nums

            if right_i <= left_i:
                return None

            if right_i - left_i == 1:
                return TreeNode(nums[left_i])
            
            if right_i - left_i > 1:
                largest = max(nums[left_i:right_i])
                largest_i = nums.index(largest)
                r_node = TreeNode(largest)

                r_node.left = helper(left_i, largest_i)
                r_node.right = helper(largest_i + 1, right_i)

                return r_node
            

        root.left = helper(0, largest_i)
        root.right = helper(largest_i + 1, len(nums))

        return root
    
class Solution2:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            node = TreeNode(num)

            while stack and num > stack[-1].val:
                node.left = stack.pop(-1)

            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]
    
print(Solution2().constructMaximumBinaryTree([2, 1, 3, 6, 0, 5]))