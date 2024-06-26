# ou are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.

 
import collections
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]

mp = collections.defaultdict(list)
for u , v in edges:
    mp[u].append(v)
    mp[v].append(u)
    
visit=set()
components = []

def find_connected_components(node):
    visit.add(node)
    res.add(node)
    
    for neigh in mp[node]:
        
        if neigh not in visit:
            
            find_connected_components(neigh)
            

def is_complelety_connected(comp):
    seen = set()
    m = len(comp)
    for c in comp:
        direct_connects = mp[c]
        for d in direct_connects:
            edge = tuple(sorted([c,d]))
            
            if edge not in seen:
                seen.add(edge)
                
    return len(seen) >= ((m*(m-1))//2)
            
            

ans = 0
for i in range(0,n):
    res = set()
    if i not in visit:
        find_connected_components(i)
        
        if is_complelety_connected(res):
            ans+=1
            
print(ans)
        
        
        
             

            