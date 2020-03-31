class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b = abs(dividend), abs(divisor)
        sign = (dividend < 0) is (divisor < 0)
        res = 0
        while a >=b:
            x = 0
            while a >=b << 1<<x:
                x+=1
            res+=1<<x
            a -= b<<x
        return min(res if sign else -res, 2147483647)
                
        
        