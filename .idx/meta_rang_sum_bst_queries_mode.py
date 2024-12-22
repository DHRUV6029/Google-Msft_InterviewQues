class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.preifx = []
        self.vals = []

    def inorderHelper(self, root):
        if not root:
            return
        
        self.inorderHelper(root.left)
        self.vals.append(root.val)

        if not self.preifx:
            self.preifx.append(root.val)
        else:
            self.preifx.append(self.preifx[-1]+root.val)

        self.inorderHelper(root.right)

    
    def bounds_search(self, target):
        l = 0
        r = len(self.vals)-1

        while l<=r:
            mid = (r+l)//2

            if self.vals[mid] == target:
                return mid   
            
            if self.vals[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return r

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l = self.bounds_search(low)
        r = self.bounds_search(high)

        if l <= 0:
            return self.preifx[r]
        else:
            return self.preifx[r] - self.preifx[l-1]
    
    

l = TreeNode(10)
l.left = TreeNode(5)
l.left.left = TreeNode(3)
l.left.right = TreeNode(7)
l.right = TreeNode(15)
l.right.right = TreeNode(18)
s = Solution()

s.inorderHelper(l)
ans = s.rangeSumBST(l , 1 , 160)
print(ans)

        
        

                
