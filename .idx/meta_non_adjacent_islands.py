import collections
import re
grid1 =[
    [1, 0, 1]
  ]



#bfs / dfs on O and make another special check if that zero has no one in its neighbour
#points to keep in mind
# add check on origin area and start wiht +1

direc = [(0,1),(1,0),(0,-1),(-1,0)]
visit = set()


def check(i , j):
    for dr , dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr , nc = i+dr, j + dc 
        
        if nr < 0 or nc < 0 or nr >= len(grid1) or nc >= len(grid1[0]):
            continue
        if grid1[nr][nc] == 1:
            return False
        
        
    return True


def find_largest_island(r, c):
    que = collections.deque()
    que.append((r,c))

    visit.add((r,c))
    area = 0
    while que:

        r, c = que.popleft()
    
        for dr , dc in direc:
            nr ,nc = r+dr , c+dc

            if nr < 0 or nc < 0 or nr >= len(grid1) or nc >= len(grid1[0])  or grid1[nr][nc] == 1 or \
                (nr ,nc) in visit:
                continue

            if check(nr,nc): 
                que.append((nr,nc))
                visit.add((nr,nc))
                area+=1

    return area
            
ans = float('-inf')
for i in range(len(grid1)):
    for j in range(len(grid1[0])):
        if (i,j) not in visit and grid1[i][j]!=1 and check(i,j):
            cur = find_largest_island(i, j)+1
            ans = max(ans,cur)

print(ans)


            

