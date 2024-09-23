# You want to run two tests on a device. Each test has a series of setup tests that must be done in order.
# For example,
# you need to complete Step A, B, and C in that order to run test1.
# Then there is test2, which needs steps X, B, and Z to be setup in that order to run.
# You could setup the device by doing the steps like this A, B, C, X, B Z. 
# But that would be inefficient because you are doing step B twice. 
# How would you make the list of steps such that there are no duplicate steps but the order of the steps is maintained. 
# For example, in this case, the optimized correct steps are A, X, B, C,Z.

import collections
print(ord('A'))
tests = {
    "Test1" : ['A', 'B' , 'C'],
    "Test2" : ['X' , 'B' , 'Z']
}

mp =  collections.defaultdict(set)

indeg = collections.defaultdict(int)
exps= set()
for test , exp in tests.items():
    for i in range(0,len(exp)-1):
        mp[exp[i]].add(exp[i+1])
        indeg[(exp[i+1])]+=1
        exps.add(exp[i])
        exps.add(exp[i+1])

que = collections.deque()

for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i in exps and indeg[i] == 0:
        que.append(i)
ans = []
while que:
    cur = que.popleft()
    ans.append(cur)

    for neigh in mp[cur]:
        indeg[neigh]-=1

        if indeg[neigh]==0:
            que.append(neigh)
            indeg.pop(neigh)
            
print(ans)


