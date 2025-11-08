# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] 
# is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, 
# so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.

from typing import List

'''
Initial Thoughts
    - reminds me of a stack like problem
    - add elements to a stack until two are the same. pop off top and keep popping until theyre different?
        - what happens if removing the first of the two same colors is better
            - we pop before pushing
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c_stack = [colors[0]]
        t_stack = [neededTime[0]]
        total_time = 0
        for color, time in zip(colors[1:], neededTime[1:]):
            if color == c_stack[-1]:
                if time < t_stack[-1]:
                    total_time += time
                    continue
                else:
                    total_time += t_stack[-1]
                    t_stack.pop(-1)
                    c_stack.pop(-1)
                    t_stack.append(time)
                    c_stack.append(color)
            else:
                c_stack.append(color)
                t_stack.append(time)

        return total_time
    
s = Solution()
print(s.minCost("abaac", [1, 2, 3, 4, 5]))