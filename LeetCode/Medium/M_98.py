# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

'''
Initial Thoughts
    - traverse the tree with inorder and build out an array with the found values
    - check if the array is the same as the sorted array.

Final Thoughts
    - I didn't account for duplicate values until the end as i just assumed binary search tree was okay
    with non unique values as long as they were next to each other. That being said, it was a quick check.

    - I think I could have been smoother with my inorder traversal and adding the vals to the list but overall 
    it wasnt too bad. 
    - I think I can improve the memory down to O(1) instead of O(N) which I will now attempt
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nextleft = None
        valid = True
        def helper(tn: TreeNode):
            nonlocal nextleft, valid
            if tn:
                helper(tn.left)
                if nextleft is None:
                    nextleft = tn.val
                else:
                    if tn.val <= nextleft:
                        valid = False
                    nextleft = tn.val
                helper(tn.right)

        helper(root)

        return valid

node3 = TreeNode(3)
node1 = TreeNode(1)
node6 = TreeNode(6)
node4 = TreeNode(4, node3, node6)
node5 = TreeNode(5, node1, node4)
node0 = TreeNode(0, None, TreeNode(-1))
node11 = TreeNode(1, node1)

print(Solution().isValidBST(node0))
    
