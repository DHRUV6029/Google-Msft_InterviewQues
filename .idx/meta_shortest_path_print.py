# Definition for a binary tree node.
import random
from typing import List
from collections import Counter, defaultdict , deque
########################
grid = [
    ['1', '1', '1', 'S', '1'],
    ['1', '1', 'X', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['X', '1', '1', 'E', '1'],
    ['1', '1', '1', '1', 'X']
]
#find S and E coordinates
def find_start_end_coordinates(grid):
    start , end = None , None
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] == 'S':
                start = (i , j)
            
            if grid[i][j] == 'E':
                end = (i ,j)

    return [start , end]


def bfs(start,end):
    visit = set()
    que = deque()
    parent = defaultdict(int)

    visit.add(end)
    que.append(end)

    while que:

        for _ in range(len(que)):
            cur = que.popleft()

            if cur[0] == start[0] and cur[1] == start[1]:
                return parent
            
            for dr ,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = cur[0]+dr , cur[1]+dc

                #check boundary conditions
                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or (nr,nc) in visit \
                    or grid[nr][nc] == 'X':
                    continue

                que.append((nr,nc))
                visit.add((nr,nc))
                parent[(nr,nc)] = (cur[0],cur[1])

    return parent

def find_path(mp , start ,end):
    ans = []

    while start != end:
        ans.append(start)
        if start in mp:
            start = mp[start]
    return ans[1:]


start , end = find_start_end_coordinates(grid)
mp = bfs(start ,end)
ans = find_path(mp , start, end)
print(ans)
