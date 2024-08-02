import collections
import heapq
s = [0, 0]
t = [1,2]

grid = [[0,0,1],[0,0,0],[0,0,0]]

#assuming there can be multiple cats

cats = collections.deque()
for i in range(0,len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j]==1:
            cats.append((i , j))
            grid[i][j] = 0   #distance from itself is zero
        else:
            grid[i][j] = -1 

def check_boundary_conditions(i , j):
    if i < 0 or j < 0 or i > len(grid)-1 or j> len(grid[0]):
        return False
    return True

def find_shortest_distance_from_all_cats():
    while cats:
        for _ in range(len(cats)):
            cur = cats.popleft()
            r ,c = cur[0]  , cur[1]

            for dr , dc in [(0,1) , (1, 0) , (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if check_boundary_conditions(nr , nc) and grid[nr][nc] == -1:
                    cats.append((nr , nc))
                    grid[nr][nc] = grid[r][c]+1



def find_max_possible_distance():
    max_heap = []
    heapq.heappush(max_heap , (-grid[s[0]][s[1]] , (s[0] , s[1])))
    grid[s[0]][s[1]] = -1

    while max_heap:
        dist , r, c = heapq.heappop(max_heap)
        dist = abs(abs)
        
        if r == t[0] and c == t[1]:
            return dist

        for dr , dc in [(0,1) , (1, 0) , (-1, 0), (0, -1)]:
            nr , nc = r + dr , c + dc

            if check_boundary_conditions(nr , nc) and grid[nr][nc] !=-1:
                heapq.heappush(max_heap , (-min(dist , grid[nr][nc]) , (nr , nc)))
                grid[nr][nc] = -1



