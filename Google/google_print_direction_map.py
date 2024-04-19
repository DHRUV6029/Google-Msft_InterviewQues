# Given an matrix populated with numbers from 1-7. Each of the number represents a direction in the entire matrix. e.g: if matrix[0][0] = 2, and if 2 represents 'B', then the only valid move is to go down.

# From the given input matrix find any single possible direction map that allows us to move from top left to bottom right cells.

# Direction map is the, map defining the direction each number means. There are only 4 valid directions. 'U' - Up, 'D' - Down, 'L' - Left, and 'R' - Right.

# Sample input:

# 1 2 6 4
# 3 1 2 3
# 7 5 4 6
# 3 7 2 1

# Output - {1: 'R', 2: 'D', 3:'L', 4: 'R', 5: 'L', 6: 'D',7:'L'} or {1: 'D', 2: 'R', 3: 'R', 4: 'D', 5: 'R', 6: 'D',7:'L'} or anything that can get us answer.
#Flaw wont print a entrie map :::::::::::

from collections import Counter, defaultdict
grid= [[1, 2, 6, 4],
       [3, 1, 2, 3],
       [7, 5, 4, 6],
       [3, 7, 2, 1]]

{1: 'R', 2: 'R', 6: 'D', 4: 'L', 3: 'D'}
#Approach 

direc_map ={
    (0,1) : 'R',
    (1,0) : 'D',
    (-1,0) : 'U',
    (0,-1) : 'L'
}

m = len(grid)
n = len(grid[0])

count = Counter()  #keeps the track of already assigned direc in the path 
seen = Counter() #keeps already visited node, means already assigned

master_map ={}
direc = defaultdict()


def backtrack(i , j):
    #base case
    if i < 0 or j < 0 or i >= m or j >= n or seen[i, j] or (i, j) == (m-1 , n-1):
        
        return (i, j) == (m-1, n-1) #return true if we are at the end 
     
    seen[i ,j] = 1
    k = grid[i][j]
    count[k] = count[k]+1
    
    for dr , dc in ([(0,1),(-1,0),(1,0),(0,-1)] * (count[k]<2)) or [direc[k]]:
        #before exploring this value we need to decided 
        #if we want a 4 direction exploration if this value is not assigned any value before
        #or if we have already assigned a directions to this node do go in that direction  
        direc[grid[i][j]] = (dr , dc)
        nr , nc = i+dr , j + dc
        if backtrack(nr , nc):
            return 1
        
    #restore the state
    seen[i , j] = 0
    count[k] = count[k] - 1
    

    return 0
            
            
backtrack(0, 0)

ans = defaultdict(int)


for v in direc:
    ans[v] = direc_map[direc[v]]
    
print(ans)

            
