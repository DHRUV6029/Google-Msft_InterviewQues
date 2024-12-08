"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #morris order traversal
        if not root:
            return root
        head = Node(1001)
        last = head
        node = root

        while node is not None:
            #go left 
            if node.left:
                #need to find the inorder Succsoers for this node and link it back
                pred = node.left  #do not move the node 

                while pred.right and pred.right != node:
                    pred = pred.right

                #case-1 right of this is nULL this is 
                if pred.right is None:
                    pred.right = node
                    node = node.left
                else:
                    #do the thing
                    last.right = node
                    node.left = last
                    last = node
                    #do the thing

                    node = node.right
            else:
                #do the thing
                last.right = node
                node.left = last
                last = node
                #do the thing

                node = node.right

        last.right = head.right

        head.right.left = last

        return head.right
