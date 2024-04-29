n = 9

dp = [0]*(n+1)

if n <=3:
    print(n-1)

dp[0]= 0
dp[1]= 1
dp[2]= 2
dp[3]= 3


for i in range(4, n+1):
    ans = 0
    for j in range(1, i+1):
        ans = max(ans , j * dp[i - j])
        
    dp[i] = ans
    
print(dp[-1])
        

