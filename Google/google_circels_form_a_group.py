circles = [[1,1,5],[10,10,5]]

class DSU:
    def __init__(self, size) -> None:
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
            
        return self.parent[node]
    
    def union(self, nodeA , nodeB):
        x = self.find(nodeA)
        y = self.find(nodeB)
        
        if x == y:
            return
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x]+=self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y]+=self.rank[x]
            
            
ans = 0


dsu = DSU(len(circles))
for i in range(0,len(circles)-1):
    for j in range(i+1,len(circles)):
        
        #check if they can be merged 
        x1,y1,r1 = circles[i]
        x2,y2,r2 = circles[j]
        
        dist = abs(x1-x2)**2 + abs(y1-y2)**2
        if dist <= (r1+r2)**2:
            dsu.union(i ,j)
            

print(len(set(dsu.parent))==1)
            