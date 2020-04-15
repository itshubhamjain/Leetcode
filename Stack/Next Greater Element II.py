class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        res = [-1]*len(nums)
        for idx in range(len(nums)-1,-1,-1):
            while stack and nums[idx]>=stack[-1]:
                stack.pop()
            if stack:
                res[idx]  = stack[-1]
            stack.append(nums[idx])
        return res