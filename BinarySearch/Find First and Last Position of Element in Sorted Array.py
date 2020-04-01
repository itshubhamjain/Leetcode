class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(low, high):
            if nums[low] == nums[high] ==target:
                return [low, high]
            if nums[low] <= target <= nums[high]:
                mid = (low + high)//2
                l, r = search(low,mid), search(mid+1, high)
                return max(l,r) if -1 in l+r else [l[0], r[1]]
            return [-1,-1]
        if not nums or len(nums)== 0:
            return [-1,-1]
        return search(0, len(nums)-1)
        
       
       