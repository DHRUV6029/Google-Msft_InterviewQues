#LCA in N-arty tree

class Node:
    def __init__(self,val =None , children =None):
        self.val = val
        self.children = children if children else []


class Solution:
    def __init__(self):
        self.parent = {}

    def LcaOfNary(self, root , p  , q):
        
        def buildChildToParent(node, par):
            self.parent[node] = par
            for child in node.children:
                buildChildToParent(child, node)


        buildChildToParent(root, None)
        
        nodea = p
        nodeb = q

        while nodea != nodeb:
            nodea = self.parent[nodea] if nodea else q
            nodeb = self.parent[nodeb] if nodeb else p

        return nodea


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# Connect nodes according to the tree structure
node3.children = [node5, node6]    # Node 3 has children 5 and 6
node1.children = [node3, node2, node4]  # Node 1 has children 3, 2, and 4


root = node1
s = Solution().LcaOfNary(root , node3 , node3)
print(s.val)

        

