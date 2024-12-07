# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        st = []
        dic = collections.defaultdict(object)

        st = [root]
        dic[root] = None

        while st:
            cur = st.pop()

            if cur.left:
                dic[cur.left] = cur
                st.append(cur.left)
            
            if cur.right:
                dic[cur.right] = cur
                st.append(cur.right)

        p1 , q1 = p , q

        while p1 != q1:
            p1 = dic[p1] if dic[p1] is not None else q
            q1 = dic[q1] if dic[q1] is not None else p

        return p1
