class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(':')',
            '{':'}',
            '[':']'
        }
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if not brackets[stack.pop()]==char:
                    return False
        
        return True if not len(stack) else False