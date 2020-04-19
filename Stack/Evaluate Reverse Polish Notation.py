class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a,b : a+b,
            '-': lambda a,b: b-a,
            '/': lambda a,b : b/a,
            '*': lambda a,b : a*b
        }
        
        for c in tokens:
            if len(c)>1 or c.isdigit():
                stack.append(int(c))
            else:
                operation = operations[c]
                stack.append(int(operation(stack.pop(),stack.pop())))
        return stack[0]