# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

# x for x >= 0.
# -x for x < 0.
points = [[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]


prev = points[0]
dp = [0]*len(points[0])

for i in range(0 ,len(points)):
    
    for j in range(0 ,len(points[0])):
        dp[j]+=points[i][j]
        
    for k in range(1,len(points[0])):
        dp[k] = max(dp[k], dp[k-1]-1)
        
    for z in range(len(points)-2,-1,-1):
        dp[z] = max(dp[z] , dp[z+1]-1)
        
        
        
        

    
print(max(dp))

  