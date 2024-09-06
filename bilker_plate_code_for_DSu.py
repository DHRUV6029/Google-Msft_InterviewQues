import collections
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
            
