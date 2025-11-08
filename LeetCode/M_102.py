# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Initial Thoughts
    - This is like a textbook BFS using a Queue problem
    - how do we determine the level of the node
        - keep track of the level when enqueing?

Concluding Thoughts
    - I liked my usage of a defaultdict(list) to keep track of the level as well as including the level as a tuple
    with the node as I enqueued it. It made it easy to keep track of and didn't take up much time or memory
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = defaultdict(list)
        queue = [(0, root)]

        if root is None:
            return []

        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node[1].left is not None:
                queue.append((curr_node[0] + 1, curr_node[1].left))
            if curr_node[1].right is not None:
                queue.append((curr_node[0] + 1, curr_node[1].right))

            output[curr_node[0]].append(curr_node[1].val)

        return list(output.values())
    
node5 = TreeNode(15)
node4 = TreeNode(7)
node3 = TreeNode(20, node5, node4)
node2 = TreeNode(9)
node1 = TreeNode(3, node2, node3)
s = Solution()
print(s.levelOrder(node1))