class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2
        prevmid = -1
        if x == 0 or x ==1  :
            return x 
        while low <= high:
            mid =  (low +high)//2
            square = mid*mid
            if square > x:
                high = mid - 1
            elif square < x:
                low  = mid + 1
            else:
                return mid
        
        return high