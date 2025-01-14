class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BstPostOrderIterator:
    # def __init__(self, root) -> None:
    #     self.last_visit_node = None
    #     self.st = []
    #     self.__populate(root)

    # def hasNext(self):  # Fixed method name
    #     return len(self.st) > 0
    
    # def next(self):
    #     node = self.st[-1]

    #     if node.right and node.right != self.last_visit_node:
    #         self.__populate(node.right)
    #         return self.next()
        
    #     val = self.st.pop().val
    #     self.last_visit_node = node  # Added this line
    #     return val

    # def __populate(self, cur):
    #     while cur:
    #         self.st.append(cur)
    #         cur = cur.left

    def __init__(self, root) -> None:
        self.st = []
        self.__populate(root)
    

    def next(self):
        node = self.st.pop()

        if self.st and  node.right == self.st[-1]:

            self.st.pop() #pop the right node
            self.st.append(node) #restack the node

            self.__populate(node.right)
            node = self.st.pop()

        return node.val




    def hasNext(self):
        return len(self.st)> 0
    
    def __populate(self, cur):
        while cur:
            if cur.right is not None:
                self.st.append(cur.right)
            
            self.st.append(cur)

            cur = cur.left
        



def createTree():
    # Create all nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    return root

root = createTree()

bst = BstPostOrderIterator(root)
print(bst.hasNext())

print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
print(bst.next())
