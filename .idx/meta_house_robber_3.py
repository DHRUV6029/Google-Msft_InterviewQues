class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mp = {-1: []}
        que= deque()
        que.append([root, -1])
        tree = []
        index = -1
        while que:
            cur , p_idx = que.popleft()
            if cur:
                tree.append(cur.val)
                index+=1
                mp[index] = [] 
                mp[p_idx].append(index)
                que.append((cur.left , index))
                que.append((cur.right , index))


        dp_rob = [0]*(index+1)
        dp_not_rob = [0]*(index+1)

        for i in range(index, -1, -1):
            if not mp[i]:
                dp_not_rob[i] = 0
                dp_rob[i] = tree[i]

            else:
                
                dp_rob[i] = tree[i] + sum(dp_not_rob[child] for child in mp[i])
                dp_not_rob[i] = sum(max(dp_rob[child] , dp_not_rob[child]) \
                                    for child in mp[i])

        return max(dp_not_rob[0] , dp_rob[0])
    
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1_left = TreeNode(1)
n3_right = TreeNode(3)
n1_right = TreeNode(1)

# Connect nodes
n3.left = n4
n3.right = n5

n4.left = n1_left
n4.right = n3_right

n5.right = n1_right

s = Solution().rob(n3)
print(s)
        
