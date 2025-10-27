# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank 
# representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, 
# consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Return the total number of laser beams in the bank.
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # figure out the empty rows
        # mult count of top row devices with bottom row devices
        # add to total
        output = 0

        # get empty row idxes
        indexes_of_empty_rows = []
        for i, row in enumerate(bank):
            if '1' not in list(row):
                indexes_of_empty_rows.append(i)
        
        # remove beginning and trailing rows of 0's
        ctr = 0
        while indexes_of_empty_rows[0] == ctr:
            indexes_of_empty_rows.pop(0)
            ctr += 1

        ctr = len(bank) - 1
        while len(indexes_of_empty_rows) > 0 and indexes_of_empty_rows[-1] == ctr:
            indexes_of_empty_rows.pop(-1)
            ctr -= 1

        # how do we want to handle the middle 
        # find start row
        # find end row which is 1 more than the number of 0 rows in a row
        while len(indexes_of_empty_rows) > 0:
            start_row = indexes_of_empty_rows[0] - 1
            end_row = indexes_of_empty_rows[0]
            indexes_of_empty_rows.pop(0)
            while len(indexes_of_empty_rows) > 0 and indexes_of_empty_rows[0] == end_row + 1:
                indexes_of_empty_rows.pop(0)
                end_row += 1
            end_row += 1
            output += list(bank[start_row]).count('1') * list(bank[end_row]).count('1')

        return output
    
solution = Solution()
print(solution.numberOfBeams(["011001","000000","010100","001000"]))

# wrong approach due to misunderstanding of the problem (count even if there is no row of 0s between)

# new approach: 
# drop all rows of 0's
# mult adjactent counts and add to output 

class Solution2:
    def numberOfBeams(self, bank: List[str]) -> int:
        output = 0

        valid_device_rows = []
        for row in bank:
            if '1' in list(row):
                valid_device_rows.append(row)
        
        for i in range(len(valid_device_rows) - 1):
            output += list(valid_device_rows[i]).count('1') * list(valid_device_rows[i + 1]).count('1')

        return output
    
solution2 = Solution2()
print(solution2.numberOfBeams(["011001","000000","010100","001000"]))

# Solution 2 passes but can it be more space efficient/faster?

# new approach:
# instead of creating a new list of rows, we do it in one pass

class Solution3:
    def numberOfBeams(self, bank: List[str]) -> int:
        output = 0
        start = 0
        end = 0

        while len(bank) > 0 and '1' not in list(bank[0]):
            bank.pop(0)

        for i, row in enumerate(bank[1:]):
            if '1' in list(row):
                end = i + 1
                output += list(bank[start]).count('1') * list(bank[end]).count('1')
                start = end

        return output
    
solution3 = Solution3()
print(solution3.numberOfBeams(["011001","000000","010100","001000"]))

# runtime O(n)
'''
This is O(n) where n is the length of the bank list as it is a single pass (broken up into two loops)
Each index of the bank list is visited once, ether to pop off the row due to it being a leading 0's row
or as it searches for the end row to multiply with the saved start row
'''

# memory O(1)
'''
This is constant memory as there are only three ints declared and the memory is not dependent on the size
of the input bank list. No lists were created.
'''