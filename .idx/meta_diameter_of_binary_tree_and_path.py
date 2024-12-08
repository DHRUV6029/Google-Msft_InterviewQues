# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        self.path = []
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return 0 #, []


            left_d  = helper(root.left)
            right_d  = helper(root.right)

            if left_d + right_d >self.diameter:
                self.diameter = left_d + right_d
                #self.path = left_p + [root.val] + right_p

            if left_d > right_d:
                return left_d+1 #,  left_p + [root.val]

            else:
                return right_d+1 #, right_p + [root.val]

        helper(root)
        
        return self.diameter #, self.path
        
