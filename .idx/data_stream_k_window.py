from traceback import print_tb


nums = [1,2,4,4,5,6,7,89]

k = 3
ans = []
cur = 0
t = 0
for i in range(0,len(nums)):
    cur+=nums[i]
    if i - k + 1>=0:
        ans.append(cur/k)
        cur-=nums[i-k+1]
        

print(ans)
    
