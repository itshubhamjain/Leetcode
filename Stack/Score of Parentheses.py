# Using Stacks
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for bracs in S:
            if bracs == '(':
                stack.append(0)
            else:
                currScore = stack.pop()
                stack[-1]+=max(2*currScore,1)
        return stack.pop()



# By Counting Cores


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = bal =0
        for idx, val in enumerate(S):
            if val == '(':
                bal+=1
            else:
                bal -=1
                if S[idx - 1] == '(':
                    ans += 1<<bal
        return ans