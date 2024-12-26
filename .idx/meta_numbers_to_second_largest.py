nums = [1,2]

arr = [0]*10
min1 , min2 = 0 ,0
for i in range(0 ,len(nums)):
    arr[nums[i]]+=1
   

ans = []
for i in range(len(arr)-1, -1 ,-1):
    ans.extend([i]*arr[i])

min1 = ans[-1]

idx1 = 0
for i in range(len(ans)-1, -1, -1):
    if ans[i] == min1:
        idx1 = i
    elif ans[i]>min1:
        ans[i] , ans[idx1] = ans[idx1] , ans[i]
        break


print(ans)
   
