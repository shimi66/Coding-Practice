# You are given an array of integers nums and the head of a linked list. 
# Return the head of the modified linked list after removing all nodes from the linked list that 
# have a value that exists in nums.

from typing import List, Optional

'''
Initial thoughts
    - pointer for last valid node
    - second pointer to iterate through and check for next valid nodes

Midway thoughts
    - solution works but TLE at 576/582
    - seeing the test case, I think the bottleneck is checking whether a val is inside the nums list

Concluding thoughts
    - I learned that membership checks on a set are on avg O(1) time rather than O(n) for lists
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        last_valid = None
        output = None
        curr = head
        nums = set(nums)

        while curr is not None:
            if curr.val not in nums:
                if last_valid is not None:
                    last_valid.next = curr
                else:
                    output = curr
                last_valid = curr

            curr = curr.next
        last_valid.next = None

        return output
    
s = Solution()
# node5 = ListNode(5)
# node4 = ListNode(4)
node3 = ListNode(9)
node2 = ListNode(10, node3)
node1 = ListNode(2, node2)
print(s.modifiedList([9, 2, 5], node1))
