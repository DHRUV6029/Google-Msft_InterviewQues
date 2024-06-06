# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_morris_traversal(root):
            res = []
            cur = root
            
            while cur is not None:

                if not k:
                    return cur.val

                if cur.left is None:
                    k-=1
                    cur = cur.right  #Do not go on left its already null
                else:
                    #####################Find Inorder Predessor of the cur Node###################
                    prev = cur.left

                    while prev.right is not None and prev.right != cur:
                        prev = prev.right
                    ##############################################################################

                    #Case-1 this node prev one as no right one so we can link back to
                    if prev.right is None:
                        prev.right = cur
                        cur = cur.left   #we were going left 

                    else:
                        #thid portion of tree is already visited
                        prev.right = None
                        k-=1
                        cur = cur.right
            return 0
        
