# For a rooted tree with any arbitary number of children for each node,
# not necessarily n-ary tree.
# Remove all the leaf nodes, and store them in a list, this would create
# new leaf nodes. Repeat untill all the nodes are removed
# Conditions : Freshly created leaf nodes(node whose children are removed)
# should not be removed just after its children are removed, unless
# there's no other option for us, then we can remove it


import collections

mp =collections.defaultdict(list)


#generating for test
N = 9
mp = {
    1 : [2,3,4],
    2 : [1],
    3 : [1],
    4 : [5,6, 7, 1],
    5 : [4],
    6 : [7,4],
    7 : [6],
    8 : [4]
    
}
ans = []
out_deg = [0]*N

for k, v in mp.items():
    out_deg[k]+=len(v)

out_deg[0]= -1

#collext the first layer leaves
que = collections.deque()

for i in range(1 , len(out_deg)):
    if out_deg[i]==1:
        que.append(i)
        
ans.append(list(que))

while que:
    _s = len(que)
    for _ in range(_s): #process the cureent level of leaf
        cur = que.popleft()
        
        for neigh in mp[cur]:
            out_deg[neigh]-=1
            
            if out_deg[neigh] == 1:
                que.append(neigh)
      
    if que:          
        ans.append(list(que))
        
        
print(ans)
                