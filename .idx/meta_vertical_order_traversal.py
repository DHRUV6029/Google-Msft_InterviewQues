# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols= collections.defaultdict(list)
        min_col , max_col = float('inf') , float('-inf')
        res = []
        def bfs(root):
            nonlocal min_col , max_col
            if not root:
                return []
            
            que = collections.deque()
            que.append((root, 0 , 0))  #the origin

            while que:
                node, r, c = que.popleft()

                if node is not None:
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)

                    cols[c].append((node.val , r))

                    que.append((node.left, r+1, c-1))
                    que.append((node.right , r+1 , c+1))

        bfs(root)

        for i in range(min_col, max_col+1):
            cols[i].sort(key=lambda x : (x[1], x[0]))
            tmp = []
            for v in cols[i]:
                tmp.append(v[0])
            res.append(tmp)
        
        return res


        #c = (1,0) , (6,2) (5,2). -> needed 1 5 5
