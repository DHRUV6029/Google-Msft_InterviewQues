# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def helper(root):
            if not root:
                return 0

            if low <= root.val <= high:
                self.res+=root.val

            if root.val > low:
                helper(root.left)
            
            if root.val < high:
                helper(root.right)

        helper(root)
        return self.res

        
