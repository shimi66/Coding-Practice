# You are given a binary string s.

# You can perform the following operation on the string any number of times:

# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. 
# For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.

'''
First Thoughts
    - we are only going to move ones starting from the left to right
        - move 1 until we create 2 ones
        - move next 1 and all previous ones
        - continue

    - dont actually need to move the 1's
        - we can just count how many 0's between blocks
        - and count how many times the blocks move

Final Thoughts
    - I cooked
'''

class Solution:
    def maxOperations(self, s: str) -> int:
        first_one = s.find('1')
        if first_one == -1 or '0' not in s:
            return 0
        block_size = 0
        operations = 0
        zero_block = False
        for i in range(first_one, len(s)):
            if s[i] == '1':
                if zero_block:
                    operations += block_size
                    zero_block = False
                block_size += 1
            else:
                zero_block = True
        
        if zero_block:
            operations += block_size
        
        return operations
    
s = Solution()
print(s.maxOperations("001110"))