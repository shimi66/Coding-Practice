# Given the head of a singly linked list where elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

'''
Initial thoughts
    - select root
        - divide problem to right and left sub problems
        - recurse

    - is there a way to do it in a single pass?
        - yes we would use pointers and build the tree in order
            - find mid
            - build left tree
            - add to mid
            - build right tree
            - add to mid

        - same idea as what i did but we would keep a pointer of the "mids" and build trees based off the indexes
        until we went in order of the nodes

Final Thoughts
    - I think it would have taken me awhile to come up with the in order O(1) space solution, however, I 
    had a solid implementation with divinding and conquering the two sub trees in the problem.
'''

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        def helper(i: int, j: int) -> Optional[TreeNode]:
            if i > j:
                return None
            elif i == j:
                return TreeNode(nodes[i].val)
            
            m = ((j-i)//2) + i
            node = TreeNode(nodes[m].val)
            node.left = helper(i, m-1)
            node.right = helper(m+1, j)
            return node

        return helper(0, len(nodes)-1)

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
s = Solution()
print(s.sortedListToBST(node1))