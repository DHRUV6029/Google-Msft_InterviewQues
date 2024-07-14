arr = [1,1,1,1]

n = len(arr)
dp = [0] * n
dp[0] = arr[0]
max_sum = dp[0]

for i in range(1, n):
    dp[i] = arr[i]
    for j in range(i):
        if i - j > max(arr[i], arr[j]):
            dp[i] = max(arr[j], dp[j] + arr[i])
        
    max_sum = max(max_sum, dp[i])

print(max_sum)
