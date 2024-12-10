from typing import Optional
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIteratorPostorder:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []

        self.postOrder_control(root)


    def next(self) -> int:
        node = self.st.pop()

        if self.st and self.st[-1] == node.right:
            #this nodes right subtree needs to be visited 
            #restack this ndoe
            self.st.pop()
            self.st.append(node)
            self.postOrder_control(node.right)
            node = node.right
            node = self.st.pop()
    
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.st) > 0

    def postOrder_control(self, root):
            
        while root:
            if root.right:
                #restack it
                self.st.append(root.right)  #this nodes right is not visited yet

            self.st.append(root) #we just visited this node right subtree above

            root = root.left
            
        
        

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

bSTIterator = BSTIteratorPostorder(root);
print(bSTIterator.next())
print(bSTIterator.next())

bSTIterator.hasNext(); 

print(bSTIterator.next())

bSTIterator.hasNext(); 

print(bSTIterator.next())  
bSTIterator.hasNext();

print(bSTIterator.next()) 
bSTIterator.hasNext(); 
print(bSTIterator.next()) 

print(bSTIterator.next()) 
