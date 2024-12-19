class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Morris Preorder Traversal
        cur = root
        count = 0
        while cur:
            if cur.left:
                # Find predecessor
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                
                if pred.right is None:
                    # First visit - PROCESS NODE HERE
                    count += 1
                    if count == k:
                        return cur.val
                    # Create link and go left
                    pred.right = cur
                    cur = cur.left
                else:  # pred.right == cur
                    # Second visit - just remove link and go right
                    pred.right = None
                    cur = cur.right
            else:
                # No left child - PROCESS NODE HERE
                count += 1
                if count == k:
                    return cur.val
                cur = cur.right
        return -1
