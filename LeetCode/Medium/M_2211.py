# There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 
# from left to right and each car is present at a unique point.

# You are given a 0-indexed string directions of length n. directions[i] can be either 
# 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, 
# or staying at its current point respectively. Each moving car has the same speed.

# The number of collisions can be calculated as follows:

# When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
# When a moving car collides with a stationary car, the number of collisions increases by 1.
# After a collision, the cars involved can no longer move and will stay at the point where they 
# collided. Other than that, cars cannot change their state or direction of motion.

# Return the total number of collisions that will happen on the road.

'''
Initial thoughts
    - we can use a stack to hold what directions cars are going and if there are crashes? 20 min

Midway thoughts
    - somehwat treated it like a stack. it is a single pass with a counter though so it should be fast?
    - re run the tests at home to see if its faster

Final thoughts
    - good practice for thinking about stack problems. I wouldn't say I used a stack but i used similar ideas to a stack and tracked it with a pointer
    instead which should be faster and more memory efficient
    - with that said, I can see how a stack would have been used
'''

class Solution:
    def countCollisions(self, directions: str) -> int:

        collisions = 0
        count = 0 # counting how many are traveling left
        idx = len(directions) - 1

        while idx >= 0 and directions[idx] == 'R':
            idx -= 1

        while idx >= 0:
            curr = directions[idx]
            if curr == 'L':
                count += 1
            elif curr == 'S':
                collisions += count
                count = 0
            elif curr == 'R':
                if count == 0:
                    collisions += 1
                else:
                    collisions += count + 1
                    count = 0
            
            idx -= 1

        return collisions