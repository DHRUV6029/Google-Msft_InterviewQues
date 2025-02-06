
def printPathFromSourceToDest(src, dest):

    path = []
    st = []
    visit = set()

    st.append(src)
    visit.add(src)
   

    direc = [(0,1),(1,0),(-1,0),(0,-1)]

    while st:
        cur = st.pop()
        path.append(cur)
        if cur[0] == dest[0] and cur[1] == dest[1]:
            return path
        
        for dr, dc in direc:
            nr = cur[0]+dr
            nc = cur[1]+dc

            if nr < 0 or nc < 0 or nr > len(maze)-1 or nc > len(maze[0])-1 or (nr, nc) in visit or maze[nr][nc] == 1:
                continue

            st.append((nr,nc))
            
            visit.add((nr,nc))

    return

def printPathFromSourceToDestRec(src, dest):
    visit = set()
    path = []
    direc = [(0,1),(1,0),(-1,0),(0,-1)]
    def dfs(r,c):
        if r<0 or c<0 or r>len(maze)-1 or c > len(maze[0])-1 or (r,c) in visit or maze[r][c]==1:
            return False

        path.append((r,c))
        visit.add((r,c))

        if r == dest[0] and c == dest[1]:
            return path

        for dr , dc in direc:
            nr = r+dr
            nc = c+dc

            res = dfs(nr,nc)
            if res:
                return True
        
        path.pop()
        return 
    
    dfs(0,0)
    return path #visit is unordered hash so path is needed
            




# Example usage
maze = [
    [0,0,0,1],
    [1,1,0,0],
    [1,1,1,0],
    [1,1,1,0]
]
n , m = len(maze)-1 , len(maze[0])-1

ans = printPathFromSourceToDestRec((0,0) , (n,m))
print(ans)
