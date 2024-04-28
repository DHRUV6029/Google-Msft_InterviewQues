arr = [8,9,10]
days = 2

def binSearch(mid):
    cnt = 0
    cur = 0
    for i in range(0,len(arr)):
        cur+=arr[i]
        
        if cur > mid:
            cur = arr[i]
            cnt+=1
        
    
            
       
        
    return cnt == days-1

l =1 
r = sum(arr)
ans = 0
while l <= r:
    mid = (l+r)//2
    
    if binSearch(mid):
        #if this is possible then try more less
        ans = mid
        r = mid-1
    else:
        l =mid+1
        
        
print(ans)