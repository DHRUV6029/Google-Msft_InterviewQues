costs = [[10,20],[30,200],[400,50],[30,20]]


costs.sort(key = lambda x: x[0]-x[1])
ans = 0
for i in range(0,len(costs)//2):
    ans = ans+ costs[i][0] + costs[i+len(costs)//2][1]
    
print(ans)