class Solution:
    def set_intersection(self, nums1, nums2):
        return [x for x in nums1 if x in nums2]
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1)< len(nums2):
            return self.set_intersection(nums1, nums2)
        else:
            return self.set_intersection(nums2,nums1)