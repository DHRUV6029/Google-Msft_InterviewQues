import heapq
grid = [[1,3,1],
        [1,1,1],
        [4,12,1]]

n = len(grid)
m = len(grid[0])

def find_minimum_path_sum():
    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
     
    minHeap = [(grid[n-1][0] , n-1 , 0)]
    dist[n-1][0] = grid[n-1][0]
    
    while minHeap:
        cur_distance , r , c = heapq.heappop(minHeap)
        
    
        
        if dist[r][c] < cur_distance:
            #we know a shorter route to this point already 
            continue
        dist[r][c] = cur_distance
        if r == 0 and c == m-1:
            return cur_distance
        for dr , dc in [(0, 1) , (-1, 0), (1, 0)]:
            nr = r+dr
            nc = c+dc
            
            #check out of bound condition
            if nr < 0 or nc < 0 or nr > n-1 or nc > m-1:
                continue
            
            heapq.heappush(minHeap , (cur_distance+grid[nr][nc] , nr, nc))
            
    return -1

ans = find_minimum_path_sum()
print(ans)

            
    
