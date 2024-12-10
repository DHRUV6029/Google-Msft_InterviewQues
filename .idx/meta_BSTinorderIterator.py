from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIteratorInorder:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []

        #init
        self.leftmost_inorder(root)
        

    def next(self) -> int:
        node = self.st.pop()

        if node.right:
            self.leftmost_inorder(node.right)

        return node.val
        

    def hasNext(self) -> bool:
        return len(self.st) > 0

    def leftmost_inorder(self, root):
        while root:
            self.st.append(root)
            root = root.left
            
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
