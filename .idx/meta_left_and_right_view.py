# A modification of level order traversal.
# Print First left side view of tree from bottom to top and 
# right side view of the tree from top to bottom.

# Definition for a binary tree node
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#use a level order travseral at each level capture at most two nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(4)

#################

que = collections.deque()
que.append(root)
level_entry =[]

while que:
    #currenty que has n leif levels 
    s , e = 0,len(que)-1
    tmp = []
    for l in range(len(que)):
        cur = que.popleft()

        if l == 0:
            tmp.append(cur.val)

        if l == e and e!=0:
            tmp.append(cur.val)

        if cur.left:
            que.append(cur.left)
        if cur.right:
            que.append(cur.right)

    level_entry.append(tmp)


ans = []

for i in range(len(level_entry)-1, -1,-1):
    ans.append(level_entry[i][0])
for i in range(0 , len(level_entry)):
    if len(level_entry[i])>1:
        ans.append(level_entry[i][1])


print(ans)

