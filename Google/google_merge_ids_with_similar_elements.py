# I had my google phone screen today and completely choked.

# You're given a list of elements. Each element has a unique id and 3 properties. Two elements are considered as duplicates if they share any
# of the 3 properties. Please write a function that takes the input and returns all the duplicates.

# Input:
# E1: id1, p1, p2, p3
# E2: id2, p1, p4, p5
# E3: id3, p6, p7, p8

# Output: {{id1, id2}, {id3}}

# Input:
# E1: id1, p1, p2, p3
# E2: id2, p1, p4, p5
# E3: id3, p5, p7, p8

# Output: {{id1, id3, id3}}

# Does anyone know how to solve this?

events = ["0 p1 p2 p3" , "1 p1 p5 p3", "2 p2 p5 p1" , "3 p3 p5 p6"]


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
            
            
#first map ids to int

mp = collections.defaultdict(int)

for event in events:
    _id = event.split(" ")[0]
    
    _events = set(event.split(" ")[1:])
    
    mp[int(_id)] = _events
    
dsu = DSU(len(mp))
for k1, v1 in mp.items():
    for k2 , v2 in mp.items():
        if k1 != k2:
            
            if v1.intersection(v2):
                dsu.union(k1, k2)
                
agg = collections.defaultdict(list)

for i in range(len(mp)):
    agg[dsu.find(i)].append(i)
    
print(list(agg.values()))     
                
    
    


            
            