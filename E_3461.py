# You are given a string s consisting of digits. Perform the following operation repeatedly until the 
# string has exactly two digits:

# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as 
# the sum of the two digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            return s[0] == s[1]
        else:
            new_s = ''
            for i in range(len(s) - 1):
                new_s += str((int(s[i]) + int(s[i + 1])) % 10)
            return self.hasSameDigits(new_s)

solution = Solution()
print(solution.hasSameDigits('3902'))

# interesting idea but does not work (failing example 510)
class Solution2:
    def hasSameDigits(self, s: str) -> bool:
        output = 0
        for i in range(len(s)):
            output += int(s[i])
        return output % 2 == 0