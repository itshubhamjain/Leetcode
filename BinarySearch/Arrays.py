class Solution:
    def findKthLargest(self, A, start1, B, start2,k):
        if start1>=len(A):
            return B[start2 + k -1]
        if start2>=len(B):
            return A[start1 + k - 1]
        if k==1:
            return min(A[start1], B[start2])
        index1 = start1 +k//2 -1
        index2 = start2 +k//2 -1
        key1 = index1 if index1 < len(A) else 99999
        key2 = index2 if index2 < len(B) else 99999
        if key1 < key2:
            return self.findKthLargest( A, start1 +k//2, B, start2,k//2)
        else:
            return self.findKthLargest( A, start1, B, start2 +k//2,k//2)
            

        
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1) + len(nums2))%2 == 0:
            return (self.findKthLargest(nums1, 0, nums2, 0, (len(nums1) + len(nums2))//2) + self.findKthLargest(nums1, 0, nums2, 0, (len(nums1) + len(nums2))//2 +1))/2
        return self.findKthLargest(nums1, 0, nums2, 0, (len(nums1) + len(nums2))//2 +1)
