# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
Initial thoughts
    - figure out how many times we are doing the reverse (divide by k)
    - for each group of k
        - save where start node points and point start node to start of next k
        - repeat for each next node and point to the one before

1 -> 2 -> 3 -> 4 with k = 3
iterate to start of next k
save end (4)
save 2
point 1 to 4
2 -> 3 -> 4
     1 -> 
save 1
save 3
point 2 to 1
     3 -> 4
2 -> 1 ->
point 3 to 2
3 -> 2 -> 1 -> 4
repeat for k nodes

Concluding Thoughts
    - I COOKED
    - Not sure if this is the easiest solution, but it was the first thing I thought of so I focused on breaking it into smaller tasks
    which helped significantly but made the code larger. Would have struggled heavily without my debugger but I was able to keep track
    of what the state of my ll looked like after each line which helped identify minor logic errors a lot quicker.

    - Just looked through some other solutions and I really like the recursive implementation of this algorithm. I briefly considered it
    to start but ended up going with a single call and handling the fixing of the tail from one group not correctly pointing to the next
    head after it had been flipped. The recursive way to resolve this issue makes so much more sense after seeing it broken down with an 
    example and I think I could have implemented it easier had I gone that route first.
'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def k_group_exists(node: ListNode, k: int) -> bool:
            curr = node
            if k == 1:
                if curr is None:
                    return False
                
            for i in range(k-1):
                if curr is None:
                    return False
                if curr.next is None:
                    return False
                curr = curr.next
            return True
        
        output = None
        current_group_start_node = head
        previous_group_end = None
        if k == 1:
            return head
        while k_group_exists(current_group_start_node, k):
            # find the target node
            target_node = current_group_start_node
            curr_node = current_group_start_node
            current_group_start_node = curr_node
            saved_node = None
            for i in range(k):
                target_node = target_node.next
            
            # perform swaps
            for i in range(k):
                saved_node = curr_node.next
                curr_node.next = target_node
                target_node = curr_node
                curr_node = saved_node
            
            # point the end of last group to the new start of this one
            if previous_group_end is not None:
                previous_group_end.next = target_node
            
            previous_group_end = target_node.next
            for i in range(k - 2):
                previous_group_end = previous_group_end.next

            # store the output
            if output == None:
                output = target_node

            # move to start of next k group
            current_group_start_node = current_group_start_node.next

        return output

solution = Solution()
node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(solution.reverseKGroup(node1, 3))

    