# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
initial thoughts
    - should be easy with a queue/stack
    - how to do it with O(n) time and O(1) space
'''

from typing import Optional
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()
        while head:
            q.append(head.val)
            head = head.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
        