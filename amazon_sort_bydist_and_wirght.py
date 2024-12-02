#assuming there are no duplictes
n = 4
weight = [3,6,5,1,1]
dist = [4,3,2,1,1]

mp = collections.defaultdict(int)
wd = []
for i in range(len(weight)):
    mp[weight[i]] = i
    wd.append((weight[i] , dist[i]))

wd.sort(key=lambda x : x[0])

next_pos = mp[wd[0][0]]+1  #never move min numbers
ans = 0
for i in range(1,len(weight)):
    cur_pos = mp[wd[i][0]]
    if cur_pos <= next_pos:
        #need to move this behind
        ans = ans +  (next_pos // wd[i][1])
        next_pos = (cur_pos + (next_pos // wd[i][1])*wd[i][1])+1



print(ans)

