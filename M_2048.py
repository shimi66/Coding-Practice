# An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

# Given an integer n, return the smallest numerically balanced number strictly greater than n.

class Solution:
    def __init__(self):
        self.balanced_nums = []

    def nextBeautifulNumber(self, n: int) -> int:
        # find next balanced_nums
        self.balanced_nums.sort()
        if len(self.balanced_nums) > 0 and  n < self.balanced_nums[-1]:
            idx = len(self.balanced_nums) - 1
            start = self.balanced_nums[idx]
            while start > n:
                idx -= 1
                start = self.balanced_nums[idx]
            ctr = self.balanced_nums[min(len(self.balanced_nums) - 1), idx + 1]
            output = self.balanced_nums[min(len(self.balanced_nums) - 1), idx + 1]

            while ctr > n:
                if self.check_num(ctr):
                    output = ctr
                ctr -= 1
            return output
            # we might have already found it
            # find first num bigger than n
            # reverse search until n
        else:
            output = n + 1
            while not self.check_num(output):
                output += 1
            return output
            # we need to find the next balanced one and add it to the list
            
    def check_num(self, n: int) -> bool:
        valid_nums = []
        digits = list(map(int, str(n)))
        if n in self.balanced_nums:
            return True
        for digit in digits:
            if digit in valid_nums:
                continue
            if digit == digits.count(digit):
                valid_nums.append(digit)
            else:
                return False
        self.balanced_nums.append(n)
        return True
    
solution = Solution()
print(solution.nextBeautifulNumber(22))
        