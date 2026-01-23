# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stck = []
        output = []
        
        def traverse(node: TreeNode):
            nonlocal stck, output

            if node:
                stck.append(str(node.val))

            if node.left is None and node.right is None:
                output.append("->".join(stck))
                stck.pop(-1)
            else:
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)

                stck.pop(-1)

        traverse(root)

        return output