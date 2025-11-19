# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Initial Thoughts
    - swap left and right and BFS the tree with a queue (2 min)

Concluding Thoughts
    - This was definitely the fastest implementation but if I was concerned about memory and the input
    tree length was small (which it is), a recursive approach could have been used.
'''

from typing import Optional
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        q = deque([root])
        while q:
            curr = q.popleft()
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)

        return root