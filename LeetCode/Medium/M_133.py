# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, 
# the first node with val == 1, the second node with val == 2, and so on. The graph is represented 
# in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list 
# describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given 
# node as a reference to the cloned graph.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import defaultdict, deque

'''
Initial thoughts
    - keep a hash map that tracks the node val and its edges
    - reconstruct the graph and return the same val as start

Concluding thoughts
    - I had some wasted computations as seen in the difference between alg 1 and alg 2 but i think the thought
    process of 1 was easy to understand first, and then optimize to a single pass in alg 2.
    - I correctly used hash tables and queues to implement BFS while storing the nodes/edges of the graph in the 
    hash table for reconstruction.
    - Overall it was a good practice for hash tables, BFS, and Linked Lists and I felt pretty good during this 
    question.
'''

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        start_node = node
        edges = defaultdict(list)
        new_nodes = {}

        # copy graph
        seen_vals = set()
        to_explore = deque()
        to_explore.append(node)
        while to_explore:
            curr = to_explore.popleft()
            seen_vals.add(curr.val)
            edges[curr.val] = []
            for neighbor in curr.neighbors:
                edges[curr.val].append(neighbor.val)
                if neighbor.val not in seen_vals:
                    to_explore.append(neighbor)
                    seen_vals.add(neighbor.val)

        # recreate nodes
        for val in edges.keys():
            if val not in new_nodes:
                new_node = Node(val)
                new_nodes[val] = new_node

        # recreate edges
        for val, neighbors in edges.items():
            for neighbor in neighbors:
                new_nodes[val].neighbors.append(new_nodes[neighbor])
        
        return new_nodes[start_node.val]
    
node3 = Node(3)
node2 = Node(2, [node3])
node1 = Node(1, [node2, node3])
node3.neighbors.append(node2)
node3.neighbors.append(node1)
node4 = Node(4)

s = Solution()
print(s.cloneGraph(node4))

'''
trying to implement creation of nodes/edges in one pass
'''

class Solution2:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        
        new_nodes = {}
        queue = deque([node])
        new_nodes[node.val] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in new_nodes:
                    new_nodes[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                new_nodes[curr.val].neighbors.append(new_nodes[neighbor.val])

        return new_nodes[node.val]
    
s2 = Solution2()
print(s2.cloneGraph(node1))