import collections
matrix = [
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 0]
]


direc = [(0,1),(0,-1),(-1,0),(1,0)]
visit = set()

def out_of_boundary(r, c):
    
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
        return True
    return False


def validator(r, c):
    if out_of_boundary(r, c):
        return False
    
    for i , j in direc:
        tr, tc = r+i , c+j
        if out_of_boundary(tr,tc):
            continue

        if matrix[tr][tc]==1:
            return False
        
    return True

def bfs(r, c):
    visit = set()
    cnt = 0
    que = collections.deque()
    que.append((r,c))
    visit.add((r, c))

    while que:
        i , j = que.popleft()

        for dr, dc in direc:
            nr , nc = i+dr , j+dc
            
            if validator(nr,  nc) and (nr,nc) not in visit and matrix[nr][nc] == 0:
                cnt+=1
                que.append((nr, nc))
                visit.add((nr,nc))

    return cnt

ans = 0
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j]==0 and validator(i ,j) and (i,j) not in visit:
            
            t = bfs(i , j)
            if t:
                ans = max(ans , t+1)

print(ans)
