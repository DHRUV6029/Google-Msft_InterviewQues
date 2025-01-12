# Definition for a binary tree node.

#this assumes thats the root elemet is from left then we go right 
#to do  the oppposite we nned to start level from +1
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightLeftZigZagSideView(self, root):
        if not root:
            return []
        que = collections.deque()
        que.append(root)

        ans = []
        level = 1


        while que:
            l = len(que)
            for i in range(0,len(que)):
                cur = que.popleft()

                if level % 2 ==0 and i == 0:
                    ans.append(cur.val)
                elif level % 2 ==1 and i == l-1:
                    ans.append(cur.val)

                

                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
            
            level+=1
        
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
s = Solution().rightLeftZigZagSideView(root)
