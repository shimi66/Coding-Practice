# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

'''
Initial Thoughts
    - add nodes to stack as we traverse
        - when we hit a leaf, add sum of joined stack 
        - pop last value of stack
'''

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stck = ''
        output = 0

        def helper(node: TreeNode):
            nonlocal output, stck
            if not node:
                return
            stck += str(node.val)
            if not node.left and not node.right:
                # we are at a leaf
                output += int(stck)
                stck = stck[:-1]
                return
        
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

            stck = stck[:-1]

        helper(root)
        return output
    
[4,9,0,5,1]
node4 = TreeNode(1)
node3 = TreeNode(5)
node2 = TreeNode(0)
node1 = TreeNode(9, node3, node4)
root = TreeNode(4, node1, node2)
print(Solution().sumNumbers(root))