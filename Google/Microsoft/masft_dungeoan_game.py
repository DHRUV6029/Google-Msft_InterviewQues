dungeon = [[0,-3]]
n , m = len(dungeon) ,len(dungeon[0])

dp = [[float('inf') for _ in range(m)] for _ in range(n)]


def getmin(cur ,r , c):
    if r >= n or c >= m:
        return float('inf')
    
    next_val = dp[r][c]
    return max(1 , next_val - cur)


for i in reversed(range(n)):
    for j in reversed(range(m)):
        
        cur = dungeon[i][j]
        
        #can go to c+1 or r+1
        right = getmin(cur, i , j+1)
        down = getmin(cur , i+1, j)
        
        next = min(right , down)
        
        if next != float('inf'):
            min_val = next
        else:
            min_val = 1 if cur >= 0 else (1-cur)
            
        dp[i][j] = min_val
        
print(dp[0][0])
        