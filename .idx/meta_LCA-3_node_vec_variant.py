from typing import List
import collections
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

# Let's understand how this works for nodes at different levels using an example:
# Copy 3
#    /   \
#   5     1
#  / \   /
# 6   2 0   
#    /
#   7
# For p=7, q=1 (Different Levels):
# CopyPath from p (7):
# 7 -> 2 -> 5 -> 3 -> 1 -> 3

# Path from q (1):
# 1 -> 3 -> 7 -> 2 -> 5 -> 3

# When p1 hits null (after 3): switches to q (1)
# When q1 hits null (after 3): switches to p (7)
# Why it works:

# Let's say:


# Path to root from p: length a
# Path to root from q: length b
# Distance from LCA to root: length c


# Balancing happens because:


# First pointer travels: a + (b-c)
# Second pointer travels: b + (a-c)
# Both end up traveling same distance
# Meet at LCA

# Example:
# CopyPath lengths:
# 7 to root: 4 steps
# 1 to root: 2 steps
# LCA(3) to root: 1 step

# First pointer: 4 + (2-1) = 5 steps
# Second pointer: 2 + (4-1) = 5 steps
# This works regardless of level differences because the switching mechanism equalizes the paths. 
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node' , vec : List[int] ) -> 'Node':

        parent = collections.defaultdict()

        for node in vec:
            if node.left:
                parent[node.left] = node
            
            if node.right:
                parent[node.right] = node

        p1, q1 = p , q
        while p1 != q1:
            p1 = parent[p1] if p1 in parent else q
            q1 = parent[q1] if q1 in parent else p

        return p1




n1 = Node(3)  # root
n2 = Node(5)
n3 = Node(1)
n4 = Node(6)
n5 = Node(2)
n6 = Node(0)
n7 = Node(8)
n8 = Node(7)
n9 = Node(4)
    
# Connect nodes
n1.left = n2        # Connect 3->5
n1.right = n3       # Connect 3->1
    
n2.left = n4        # Connect 5->6
n2.right = n5       # Connect 5->2
    
n3.left = n6        # Connect 1->0
n3.right = n7       # Connect 1->8
    
n5.left = n8        # Connect 2->7
n5.right = n9       # Connect 2->4
    
    


s = Solution().lowestCommonAncestor(n1 , n2 , [n3,n2,n1,n7,n9,n5,n6,n4,n8])
print(s.val)
