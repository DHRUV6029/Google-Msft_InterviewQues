# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
import bisect , heapq
########################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, cur_num , neg_count):
            if not root:
                return 0
            
            #build the cur_num
            cur_num = cur_num * 10 + abs(root.val)
            if root.val < 0:
                neg_count+=1

            if not root.left and not root.right:
                #this is a leaf node decide to add or subtract

                if neg_count % 2 == 0:
                    self.res = self.res + cur_num
                else:
                    self.res = self.res - cur_num


            #recurse on the left subtree
            return helper(root.left ,  cur_num , neg_count) + \
            helper(root.right, cur_num , neg_count)
        



                


        helper(root, 0, 0)
        return self.res
        
        

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(-2)
t.left.left = TreeNode(2)

s = Solution().sumNumbers(t)
print(s)


