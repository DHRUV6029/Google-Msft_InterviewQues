from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = [root]


    def next(self) -> int:
        node = self.st.pop()
        self.preorder_control(node)

        return node.val
        

    def hasNext(self) -> bool:
        return len(self.st) > 0

    def preorder_control(self, root):
            
        if root.right:
            self.st.append(root.right)

        if root.left:
            self.st.append(root.left)
            
        
        

root = TreeNode(7)
root.left = TreeNode(3)

root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bSTIterator = BSTIterator(root);
print(bSTIterator.next())
print(bSTIterator.next())

bSTIterator.hasNext(); 

print(bSTIterator.next())

bSTIterator.hasNext(); 

print(bSTIterator.next())  
bSTIterator.hasNext();

print(bSTIterator.next()) 
bSTIterator.hasNext(); 

