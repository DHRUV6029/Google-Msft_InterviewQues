dp = [0]*len(weight)

cur_max = weight[0]

#partition of len 1 cannot be formed
for i in range(1, len(weight)):
    cur_max = max(cur_max , weight[i])
    if cur_max == weight[i]:
        dp[i] = dp[i-1]
    else:
        dp[i]  = 1 + dp[i-1]
        cur_max = 0  #segment ends resettng the curmax


print(dp[-1])
