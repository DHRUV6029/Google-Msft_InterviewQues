
# 6. You are given a list of user sessions where each user session has start and end times both inclusive. Now, given a value N, find the count of all users at each point in time from [0,N) i.e include 0 but exclude N. Example:
# Input:
# [(0,3), (1,4) ] N=7
# Output:
# 0->1
# 1->2
# 2->2
# 3->2
# 4->1
import collections
N = 7
arr = [(0,3), (1,4)]


count = [0]*(N+1)

for s , e in arr:
    count[s]+=1
    count[e+1]-=1
    

cur = 0
t  = 0

for i in range(0,len(count)):
    cur += count[i]
    print(str(t)+ "  ----> " + str(cur))
    t+=1
 

  
    
    
