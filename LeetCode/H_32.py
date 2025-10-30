# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.


'''
Initial thoughts
    - could we drop invalid parenthese (starting with ')' or ending with '(')
    - then cound open vs closed
    - if not equal, remove from ends?

    - second thought, a solution always has to start from '()' and expand out
    - could we find all '()' and then expand as large as we can?

    - use a sliding window of growing size and build up a dp solution with a hash map to store the combinations we've seen?

End of Attempt thoughts
    - I definitely did not figure out the right algorithm to solve this efficiently, but I did come up with an algorithm
    that works until 1800 chars when it times out in leetcode.
    - If I had to guess, come form of 
    - i think i just came up with the right algorithm and am going to attempt it again now
        - did not cook but maybe have another idea
            - solves some but not all

Concluding thoughts
    - I think I couldv'e tried to use a stack given the information I had, however I don't think I would have thought of 
    pushing the indicies onto/off the stack, though it does make a lot of sense after going through the solution and 
    implementation

    - reading through the dp solution, it took me a lot longer to understand why it works.
        - if its a closing, then we have 2 scenarios
            - previous char is open and we are sure about the last 2 being a valid parentheses

            - previous char is also a closing and then we have to check a bunch of conditions to see if there 
            is a valid open one futher back

    - even with that, I think its a lot less easy to see how far back we need to check and why it ensures that 
    we will now have our longest valid parentheses
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def prune(input: str) -> str:
            while len(input) > 0 and input[0] == ')':
                input = input[1:]   
            while len(input) > 0 and input[-1] == '(':
                input = input[:-1]  
            return input                    
        # early pruning
        s = prune(s)
        
        # dict structure: {str: int} where int represents the difference in counts of open/closed parenthese
        # if balance is positive we have more open, if negative we have more closed
        dp = {}
        new_dp = {}
        outputs = []
        
        def update_dp(input: str):
            if input in dp.keys():
                return

            # if balance is positive we have more open, if negative we have more closed
            balance = input.count('(') - input.count(')')
            if balance == 0:
                dp[input] = len(input)/2
            else:
                dp[input] = balance

        for window_size in range(1, len(s) + 1):
            for window_num in range(0, len(s) - window_size + 1):
                if len(dp.keys()) == 2 ** window_size:
                    break
                curr_s = s[window_num: window_num + window_size]
                # while window size > 1 we can use what we built in our dp map
                if window_size > 1: 
                    if curr_s not in dp.keys():
                        if curr_s[-1] == '(':
                            if dp[curr_s[:-1]] < 0:
                                new_dp[curr_s] = -1
                            else:
                                new_dp[curr_s] = dp[curr_s[:-1]] + 1
                        else:
                            new_dp[curr_s] = dp[curr_s[:-1]] - 1
                else:
                    update_dp(curr_s)
            if window_size > 1:
                for key, val in dp.items():
                    if val == 0:
                        outputs.append(key)
                dp = new_dp
                new_dp = {}

        for key, val in dp.items():
            if val == 0:
                outputs.append(key)

        output = 0
        for o in outputs:
            if len(o) > output:
                output = len(o)
        return output
    
# solution = Solution()
# t = "(()(()))())))())))(((()(())))(()())((())((()()()(())))))()(())))())))(())())())((())))((((()))((())()))()(()()(())))())())))()))(()()((()(())()))((())(((()()()(((())((()()((())()))(()(())))()()))(()()))))))))((()())((((())(())())((())((()))))((()()(())()))()())((()((()))(()((())()()))((()()(()(()((())))()((())((()))()(()))())(()()())())()())(()()))))((()())(())()((()))(()(((())()(())))(())())))()))())))()()((()(((()(())(())))((()))())())())))))))((()(((())(())))(((())(()((()))))))())())()((()()((()()(())((()(((()((()())(()())()()()))()(()(()(()(((((()()))(((()))(()((()((((((()())(()))())((()))())()())()((()))())))()(()(()()))()((())())((()((())(()((())((()))))((((((((())()())))()))())((())())())()()())))))(()))()())(())(((((())((()))((()()())()))))(())))))(()(((((((())((()((()))((())((((())))))))))()))))))(()(())))))((()))(()))(()))((()((())((()(()((()(())(()()())())()))()())()(()))))(()())()()))(()())))(()))))((()()))(()()()())))))(())()()(((()()()()((())(()()())(((()(()((((()(())())))()(((()(()())))())())(()))()))())())(()()()()()())())(())((((())((((((((((()())()))())))())()))))))()(()((((((()))))))()())((()())())(()())()()()))(())()(()(()()))()))(((()(((())())()((())()))(()()((((())()))))(()(((())((())(())())()))((())(())())()(()()(())()())(()()))())()))()())()((()(((()((()()(()())))))()(()((((((((()())))(()(()))((((()()))))))))((()()(()(())(()())(((()))(())))))())(((((()((())())()())()()())()())()())))((()(()()))(((()()((())())((()(()(()())(((((()()(())))))())(())(())(()(()))(())()()))(()))(())()())((((())()())())))))()(())))()(())(())))((()()()((())()(())(()((((()))())())()(()()())()())()(()(()(()))(()(()()((())(()())))(((()(())()())(())()))(())()))())())((((()()(()))())))))))(((()))(()(()()))))))))((()))(()((()))(((((()()()))((((()()(()())((()(())))())(((()(()()))(((())()))(("
# print(len(t))
# print(solution.longestValidParentheses(t))

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        def prune(input: str) -> str:
            while len(input) > 0 and input[0] == ')':
                input = input[1:]   
            while len(input) > 0 and input[-1] == '(':
                input = input[:-1]  
            return input                    
        # early pruning
        s = prune(s)

        # get balance of open/close
        # move accordingly if not balanced
        balance = s.count('(') - s.count(')')
        removed_left = ''
        removed_right = ''
        while balance != 0:
            if balance > 0:
                # move start up until next valid (
                removed_left += s[0]
                s = s[1:]
                while s[0] != '(':
                    removed_left += s[0]
                    s = s[1:]
            if balance < 0:
                # move tail back until next valid )
                removed_right += s[-1]
                s = s[:-1]
                while s[-1] != ')':
                    removed_right += s[-1]
                    s = s[:-1]

            # recompute balance
            balance = s.count('(') - s.count(')')
        
        return max(len(s), self.longestValidParentheses(removed_left), self.longestValidParentheses(removed_right))
    
# solution2 = Solution2()
# t = "(())()(()(("
# print(len(t))
# print(solution2.longestValidParentheses(t))

class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        output = 0

        for i in range(len(s)):
            c = s[i: i+1]
            if c == "(":
                stack.append(i)
            else:
                if len(stack) > 1:
                    stack.pop(-1)
                    output = max(output, i - stack[-1])
                else:
                    stack[0] = i

        return output


solution3 = Solution3()
t = ")()())"
print(len(t))
print(solution3.longestValidParentheses(t))

class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        max_length = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                max_length = max(max_length, dp[i])
        
        return max_length
    
solution4 = Solution4()
t = "(()(()))"
print(len(t))
print(solution4.longestValidParentheses(t))