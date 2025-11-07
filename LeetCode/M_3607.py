# You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

# These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element 
# connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or 
# indirectly connected form a power grid.

# Initially, all stations are online (operational).

# You are also given a 2D array queries, where each query is one of the following two types:

# [1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. 
# If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. 
# If no operational station exists in that grid, return -1.

# [2, x]: Station x goes offline (i.e., it becomes non-operational).

# Return an array of integers representing the results of each query of type [1, x] in the order they appear.

# Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it 
# offline does not alter connectivity.

from typing import List

'''
Initial Thoughts
    - why are the directions for this one so complicated
    - maybe create a dictionary with the following structure: station: (online/offline, [stations in grid])
        - concerns, creating the 'stations in grid' may be time consuming
        - maybe hash map for the online/offline and then sets for the power grids
            - join sets together

Midway thoughts
    - TLE after 667 / 671 completed
    - I think it is due to how I am building the connections rather than how I handle the queries.
    - what if i just have c number of sets and have them be equal and then take a set of the list of sets at the end
        - did not work

Concluding thoughts
    - walked through the bfs/dfs adjacency list creation as well as how to use sorting and some other tricks to really improve
    the time complexity of this solution. 
    - I think I came up with a decent solution for a first try and knew where my issues were but I need to practice more
    with creating adjacency lists/why you use them. I should also continue to practice with my graph traversal.
    - Things to continue to practice with:
        - DSU (Disjoint Set Unions)
        - BFS/DFS
        - Queues
'''

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        output = []
        power_grids = []
        operational = {}
        for i in range(1, c+1):
            operational[i] = True
            power_grids.append(set([i]))

        for conncection in connections:
        #     joined_set = power_grids[conncection[0] - 1].union(power_grids[conncection[1] - 1])
        #     power_grids[conncection[0] - 1] = joined_set
        #     power_grids[conncection[1] - 1] = joined_set

        # pgs = []
        # for grid in power_grids:
        #     for pg in pgs:
        #         if grid & set(pg):
        #             tmp = pg.union(grid)
        #             pgs.append(tmp)
        #         else:
        #             continue
        #     else:
        #         pgs.append(grid)

            i1, g1 = None, None
            i2, g2 = None, None
            for idx, grid in enumerate(power_grids):
                if conncection[0] in grid:
                    g1 = grid
                    i1 = idx
                if conncection[1] in grid:
                    g2 = grid
                    i2 = idx
            
            if i1 == i2:
                continue
            power_grids[i1] = g1.union(g2)
            power_grids.pop(i2)

        for query in queries:
            if query[0] == 1:
                curr_station = query[1]
                min_id = None
                curr_grid = None
                for grid in power_grids:
                    if query[1] in grid:
                        curr_grid = grid
                        break

                while operational[curr_station] == False:
                    if min_id == None:
                        min_id = min(curr_grid)
                    else:
                        tmp = [station for station in grid if station > min_id]
                        if len(tmp) == 0:
                            curr_station = -1
                            break
                        min_id = min(tmp)

                    curr_station = min_id

                output.append(curr_station)
            elif query[0] == 2:
                operational[query[1]] = False
        

        return output
    
s = Solution()
print(s.processQueries(3, [[2,3],[1,2],[1,3]], [[1,1],[1,2],[1,2],[1,3],[1,3],[1,1],[2,3],[1,1],[2,2],[2,2],[1,2],[1,3],[2,1],[2,1],[1,3],[2,1],[2,3],[1,3],[1,3],[2,2],[1,1],[2,2],[1,2],[1,1],[1,2],[1,3],[1,2],[1,3],[2,2],[2,2],[2,3],[1,3],[1,2],[2,3],[1,2],[2,3],[2,3],[2,2],[2,2],[1,1],[2,3],[1,1]]))


from collections import deque, defaultdict
import bisect
from typing import List

class Solution2:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ---------- Step 1: Build adjacency list ----------
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # ---------- Step 2: Build connected components (power grids) ----------
        visited = set()
        grids = []              # list of lists, each list = a connected grid
        node_to_grid = {}       # maps station id -> grid index

        for i in range(1, c + 1):
            if i not in visited:
                queue = deque([i])
                component = []
                visited.add(i)

                # BFS to gather all stations in this grid
                while queue:
                    node = queue.popleft()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

                # sort the component so we can use bisect later
                component.sort()
                for node in component:
                    node_to_grid[node] = len(grids)
                grids.append(component)

        # ---------- Step 3: Initialize operational tracking ----------
        # All stations start operational
        operational = {i: True for i in range(1, c + 1)}
        # Each grid starts with all its stations active
        active_nodes = [grid.copy() for grid in grids]

        # ---------- Step 4: Process queries ----------
        results = []

        for query in queries:
            type_, x = query

            if type_ == 1:
                # Maintenance check
                grid_id = node_to_grid[x]
                active = active_nodes[grid_id]

                if operational[x]:
                    # If station x is operational, it handles the check
                    results.append(x)
                else:
                    # Otherwise, find smallest operational node in same grid
                    if active:
                        results.append(active[0])  # smallest ID in sorted list
                    else:
                        results.append(-1)        # none operational

            elif type_ == 2:
                # Take station x offline
                if not operational[x]:
                    continue  # already offline, skip

                operational[x] = False
                grid_id = node_to_grid[x]
                active = active_nodes[grid_id]

                # Remove x from sorted active list using bisect
                idx = bisect.bisect_left(active, x)
                if idx < len(active) and active[idx] == x:
                    active.pop(idx)

        return results
    
s2 = Solution2()
print(s2.processQueries(3, [[2,3],[1,2],[1,3]], [[1,1],[1,2],[1,2],[1,3],[1,3],[1,1],[2,3],[1,1],[2,2],[2,2],[1,2],[1,3],[2,1],[2,1],[1,3],[2,1],[2,3],[1,3],[1,3],[2,2],[1,1],[2,2],[1,2],[1,1],[1,2],[1,3],[1,2],[1,3],[2,2],[2,2],[2,3],[1,3],[1,2],[2,3],[1,2],[2,3],[2,3],[2,2],[2,2],[1,1],[2,3],[1,1]]))
