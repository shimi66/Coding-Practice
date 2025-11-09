# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Initial Thoughts
    - preorder traversal (node -> child left -> child right)
    - inorder traversal (child left -> node -> child right)

    - root will always be first in pre order
    - next preorder traversal is child left only if it is left of root in the in order traversal
        - can split in order based on curr node?
        - if following two nums in pre order are in different lists, they are the left/right children

    - USE RECURSION

Midway thoughts
    - I thought I cooked and I kind of did, I pass 202/203 and got TLE on the last test case

Final thoughts
    - I did not learn my lesson about recursion taking lots of time when creating new objects etc
    - I should have tried doing the recursion and look ups without changing the preorder and inorder lists,
    instead using pointers and a hash map index to quickly find the needed indicies

    - once reading and stepping through the algorithm, I was able to implement it on my own without any issues
'''

# take first preorder
# find first preorder in inorder and split
# increment preorder until element is not in left inorder split
# we now have two new preorder and inorder lists
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        inorder_left = inorder[0: inorder.index(root.val)]
        inorder_right = inorder[inorder.index(root.val) + 1:]
        preorder_left = []
        preorder_right = []

        for i in range(1, len(preorder)):
            if preorder[i] not in set(inorder_left):
                preorder_left = preorder[1:i]
                preorder_right = preorder[i:]
                break
        else:
            preorder_left = preorder[1:]

        if len(preorder_left) > 0:
            root.left = self.buildTree(preorder_left, inorder_left)
        if len(preorder_right) > 0:
            root.right = self.buildTree(preorder_right, inorder_right)

        return root
    
s = Solution()
print(s.buildTree([1, 2], [2, 1]))

# take first preorder
# find first preorder in inorder and split
# increment preorder until element is not in left inorder split
# we now have two new preorder and inorder lists
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we need our inorder index map
        # we need our helper function
        idx_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_bounds: int, right_bounds: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left_bounds > right_bounds:
                return None

            node = TreeNode(preorder[pre_idx])
            pre_idx += 1

            split_idx = idx_map[node.val]
            node.left = helper(left_bounds, split_idx - 1)
            node.right = helper(split_idx + 1, right_bounds)
            
            return node

        return helper(0, len(preorder) - 1)

s2 = Solution2()
print(s2.buildTree([3,9,20,15,7], [9,3,15,20,7]))