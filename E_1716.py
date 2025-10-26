# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. 
# On every subsequent Monday, he will put in $1 more than the previous Monday.

# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

class Solution:
    def totalMoney(self, n: int) -> int:
        output = 0
        num_weeks = n // 7
        remaining_days = n % 7
        for week in range(num_weeks):
            output += 28 + (7 * week)
        for day in range(remaining_days):
            output += 1 + num_weeks + day
        return output

solution = Solution()
print(solution.totalMoney(10))
    # cheap math, divide by 7 and add 28 + 7i where i is what the you get from dividing 7
    # then add remaining