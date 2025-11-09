# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Initial thoughts
    - Same as 102, this time i need a boolean/some way to track if I am queueing left to right or right to left
    - maybe just mod 2 the level
    - queue from the front when odd?

Midway thoughts
    - im so dumb
    - just do same solution as 102 and reverse every odd row

Concluding thoughts
    - I started making it more difficult with how I was changing the enqueue process. I think my original thoguht would 
    have been much more difficult to implment, however I am glad I realized it was way too complicated and could just
    reverse every other row from my previous solution.
'''

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        output = []
        queue = [(0, root)]

        if root is None:
            return []
        
        while len(queue) > 0:
            curr_node = queue.pop(0)
            if curr_node[1].left is not None:
                queue.append((curr_node[0] + 1, curr_node[1].left))
            if curr_node[1].right is not None:
                queue.append((curr_node[0] + 1, curr_node[1].right))

            d[curr_node[0]].append(curr_node[1].val)
            
        
        for level, nodes in d.items():
            if level % 2 == 0:
                output.append(nodes)
            else:
                output.append(nodes[::-1])

        return output


node5 = TreeNode(15)
node4 = TreeNode(7)
node3 = TreeNode(20, node5, node4)
node2 = TreeNode(9)
node1 = TreeNode(3, node2, node3)
s = Solution()
print(s.zigzagLevelOrder(node1))