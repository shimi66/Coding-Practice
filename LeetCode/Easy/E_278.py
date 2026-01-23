# You are a product manager and currently leading a team to develop a new product. Unfortunately, 
# the latest version of your product fails the quality check. Since each version is developed 
# based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n: int) -> bool:
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        first_bad = n

        while isBadVersion(first_bad):
            # begin binary search
            mid = ((high - low) // 2) + low
            if low >= high:
                return first_bad
            if isBadVersion(mid):
                # search first half
                high = mid
                first_bad = mid
            else:
                # search second half
                low = mid + 1
            
        return first_bad + 1
    


        