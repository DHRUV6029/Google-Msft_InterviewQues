#Given a Binary Tree with Zeros and Ones,
#find number of islands.
# Island is defined as connected nodes with only ones.

cnt = 0
def count_islands(root):
    if not root:
        return 0
    
    root.val = 0
    
    count_islands(root.left)
    count_islands(root.right)
    
    
def traverse(node):
    if not node:
        return
    
    if node.val == 1:
        cnt+=1
        
        dfs(node)
        
    traverse(node.left)
    traverse(node.right)
    
    
print(cnt)




