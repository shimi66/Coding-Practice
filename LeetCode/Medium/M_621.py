# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any 
# order, but there's a constraint: there has to be a gap of at least n intervals between two tasks 
# with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

from typing import List
from collections import Counter

'''
Initial Thoughts
    - Get the counts of all letters
    - start with the highest counts, and add letters to a set if not already in the set 
    by highest count. 
    - return num of operations

Midway Thoughts 25 min
    - struggling with the heap to keep counts sorted
    - Figured out a solution (32 min) but poor runtime. lets see if i can improve it

Final Thoughts 
    - I understood the greedy algorithm and had a decent idea for how to approach it by using the letter
    with the highest count when possible but it had trouble with runtime due to the reordering of the 
    letter with the highest count
    - the solution below now makes sense to me as it is essentially doing the same thing but from a math perspective
        - what is the minimum amount of operations it would take for me to schedule all tasks for the letter
        with the highest count. Account for multiple letters having that same count
        - Either we can fit all the other operations between the most efficient scheduling of the max count letter
        (this is the case where the most efficient scheduling of the max count letter takes the most operations
        and is the right hand side of the max below) or, we cannot fit all the operations between the most efficient
        schduling (which would mean that we can schedule all tasks without ever needing an idle so the answer would
        be # of tasks or the left hand side of the max below)
'''

class Solution(object):
    def leastInterval(self, tasks, n):
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        f_max = max(count.values())
        max_count = sum(1 for v in count.values() if v == f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + max_count)

print(Solution().leastInterval(["A","C","A","B","D","B"], 2))

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        memory = []
        operations = 0
        counts = Counter(tasks)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        while sorted_counts:
            for ltr, val in sorted_counts:
                if ltr not in memory:
                    operations += 1
                    memory.append(ltr)
                    if len(memory) > n:
                        memory.pop(0)
                    
                    idx = sorted_counts.index((ltr, val))
                    sorted_counts[idx] = (ltr, val - 1)
                    if val == 1:
                        sorted_counts.pop(idx)
                    if idx + 1 < len(sorted_counts) and sorted_counts[idx + 1][1] > sorted_counts[idx][1]:
                        offset = 2
                        while idx + offset < len(sorted_counts) and sorted_counts[idx + offset][1] > sorted_counts[idx][1]:
                            offset += 1
                        # swap idx's
                        offset -= 1
                        tmp = sorted_counts[idx]
                        sorted_counts[idx] = sorted_counts[idx + offset]
                        sorted_counts[idx + offset] = tmp
                    break
            else:
                memory.append('')
                if len(memory) > n:
                    memory.pop(0)
                operations += 1

        
        return operations
