# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the 
# product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        low = 0
        high = num
        
        while high * high > num:
            if low > high:
                return False
            mid = ((high-low)//2) + low
            if mid * mid > num:
                high = mid - 1
            else:
                low = mid + 1

        if high * high == num:
            return True
        
        return False
    
print(Solution().isPerfectSquare(9))