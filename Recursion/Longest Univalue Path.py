# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0
        def uniValueLength(node):
            if not node :
                return 0 
            left = uniValueLength(node.left)
            right = uniValueLength(node.right)
            left_uni = right_uni = 0 
            if node.left and node.left.val == node.val :
                left_uni =left + 1
            if node.right and node.right.val == node.val :
                right_uni = right + 1
            self.result = max(self.result, left_uni +right_uni)
            return max(left_uni, right_uni)
        uniValueLength(root)
        return self.result