class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, start, end):
            if start >=end:
                return 
            temp = s[start] 
            s[start] = s[end]
            s[end] = temp
            helper(s, start+1, end -1)
        helper(s, 0, len(s)-1)
        return s