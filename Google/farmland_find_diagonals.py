# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
import collections
land = [[1]]

visit = set()
def bfs(r , c):
    
    que = collections.deque()
    que.append((r, c))
    visit.add((r ,c))
    path = [(r, c)]
    while que:
        i, j = que.popleft()
        
        for dr , dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr = i + dr
            nc = j + dc
            
            if nr < 0 or nc < 0 or nr > len(land)-1 or nc > len(land[0])-1 or (nr ,nc ) in visit or land[nr][nc]==0:
                continue
            
            que.append((nr, nc))
            visit.add((nr,nc))
            path.append((nr, nc))
            
   
    path.sort(key=lambda x : (x[0] , x[1]))
    
    return [path[0][0], path[0][1] ,path[-1][0] , path[-1][1]]

ans = []
for x in range(0,len(land)):
    for y in range(0,len(land)-1):
        if land[x][y] == 1 and (x, y) not in visit:
            val = bfs(x,y)
            ans.append(val)

print(ans)            