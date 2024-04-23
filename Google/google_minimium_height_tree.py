import collections
n = 4
edges =  [[1,0],[1,2],[1,3]]

mp = collections.defaultdict(set)
out_deg = [0]*n
for u , v in edges:
    mp[u].add(v)
    mp[v].add(u)
    out_deg[u]+=1
    out_deg[v]+=1
    


que =  collections.deque([i for i in range(len(out_deg))if out_deg[i] == 1])

        
        
remian = n
while remian>2:
    remian-=len(que)
    
    new_que = []
    
    while que:
        node = que.popleft()
        
        neigh = mp[node].pop() #edge removal
        mp[neigh].remove(node) #edge removal
        
        if len(mp[neigh])==1:
            new_que.append(neigh)
            
    que = collections.deque(new_que)
    
print(que)
        