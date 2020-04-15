class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            print(arr[i-1:i]+arr[i+1:i+2])
            res += min(arr[i-1:i]+arr[i+1:i+2])*arr.pop(i)
        return res





class Solution:
def mctFromLeafValues(self, arr: List[int]) -> int:
    res = 0
    stack = [float('inf')]
    for val in arr:
        while stack[-1] <= val:
            mid = stack.pop()
            res += mid * min(val,stack[-1])
        stack.append(val)
    while len(stack)>2:
        res += stack.pop()*stack[-1]
    return res
