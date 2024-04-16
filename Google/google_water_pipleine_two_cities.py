# I got the following question in the phone screen at Google:

# Given is a 2D array that describes the height of a landscape and the location of 2 cities within this 2D array. I am now looking for the highest position to place a water tower there so that both cities can be supplied with water.
# Rules:
# The pipes of the tower are not allowed to run diagonally
# The pipes must always slope downwards (i.e. be lower than the previous cell) or be at the same height, otherwise the water would run upwards
# Inputs:
#Approach

import collections 

heights = [
[4, 9, 7, 6, 5],
[2, 6, 5, 4, 3],
[6, 5, 1, 2, 8],
[3, 4, 7, 2, 5]
]

town1 = [0,2]
town2 = [1,4]

def find_longest_path(src):
    visit = set()
    que = collections.deque()
    
    visit.add(tuple(src))
    que.append(src)
    
    direc = [(0,1),(0,-1),(-1,0),(1,0)]
    
    while que:
        cur = que.popleft()
        
        for dr , dc in direc:
            nr = cur[0]+dr
            nc = cur[1]+dc
            
            #checj valid bioundary validity
            if nr < 0 or nr > len(heights)-1 or nc < 0 or nc > len(heights[0]) -1 or (nr, nc) in visit or heights[nr][nc]<heights[cur[0]][cur[1]]:
                continue
            
            visit.add((nr, nc))
            que.append((nr, nc))
            
    return visit


pipline1 = find_longest_path(town1)
pipline2 = find_longest_path(town2)

max_val = 0
max_idx = None
for point in pipline1:
    if point in pipline2:
        point = list(point)
        if heights[point[0]][point[1]] > max_val:
            max_val =heights[point[0]][point[1]]
            max_idx = point
            
print(max_idx)
print(max_val)
             
            
    
    

