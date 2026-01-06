# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next 
# node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

'''
Initial Thoughts
    - Use stack to track dfs traversal and go until stack is None

Final Thoughts
    - Realized I was having trouble with stack due to the preorder traversal order, so I created a helper function
    that recursively added to the order
    - This is still a dfs solution as it traverses the left branch all the way first before going back up and further down
'''

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        order = [TreeNode]
        
        def helper(curr: TreeNode):
            nonlocal order
            if not curr:
                return
            
            order.append(curr)
            helper(curr.left)
            helper(curr.right)

        helper(root)

        for i in range(len(order)):
            if i == len(order) - 1:
                order[i].left = None
                order[i].right = None
                break
            else:
                order[i].left = None
                order[i].right = order[i+1]

        return order[0]

        
