# Definition for a binary tree node.
# You are given a m x n grid, where you start at the top-left cell [0,0] 
# and your goal is to reach 
# the bottom-right cell [m-1,n-1]. You are only allowed to move either 
# down or to the right at any point in time.
# Write a function that returns all possible paths from [0,0] 
# to [m-1,n-1]. For each step, store "D" if you move down and "R" if you move right.
m = 3
n = 3
ans = []
def all_paths_from_source(r , c, path):
    if r == m-1 and c == n-1:
        ans.append("".join(path))
        return
    
    #boundary conditions
    if r < 0 or c < 0 or r >= m or c >= n:
        return
    
    #move down
    path.append("D")
    all_paths_from_source(r+1 , c , path)
    path.pop()

    #move right
    path.append("R")
    all_paths_from_source(r , c+1 , path)
    path.pop()

all_paths_from_source(0,0,[])
print(ans)
