# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

from typing import List

'''
Initial thoughts
    - store a hash map in the class definition that saves the count of 1s for each number
'''

class Solution:
    hm = {}

    def countBits(self, n: int) -> List[int]:
        output = []
        
        def helper(num: int) -> int:
            if num in self.hm:
                return self.hm[num]
            
            self.hm[num] = num.bit_count()
            return self.hm[num]
            
        for i in range(n + 1):
            output.append(helper(i))

        return output
    
print(Solution().countBits(5))