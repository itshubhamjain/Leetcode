class Solution:
    def decodeString(self, s: str) -> str:
            stack = []; currNum = 0; currStr = '';  
            for c in s:
                if c == '[':
                    stack.append(currStr)
                    stack.append(currNum)
                    currNum = 0
                    currStr = ''
                elif c == ']':
                    num = stack.pop()
                    prevStr = stack.pop()
                    currStr = prevStr + currStr* num
                elif c.isdigit():
                    currNum = currNum*10 + int(c)
                else:
                    currStr +=c
            return currStr