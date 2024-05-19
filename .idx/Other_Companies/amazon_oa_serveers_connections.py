def get_min_connect_time(servers , n):
    servers.sort()
    diff = 0
    max_diff = float('-inf')
    for i in range(0,len(servers)-1):
        diff+=abs(servers[i+1]-servers[i])
        max_diff = max(max_diff,abs(servers[i+1]-servers[i]))
        
    a = n - servers[-1]
    b = servers[0] -1 
    diff+=(a+b+1)
    
    max_diff = max(max_diff,(a+b+1))
    
    return diff-max_diff


print(get_min_connect_time([2,6,8] , 8))
print(get_min_connect_time([1,5] , 5))
print(get_min_connect_time([4,6,2,9] , 10))

    
    
        
