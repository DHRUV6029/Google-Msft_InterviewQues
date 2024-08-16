# Given a integer array 'a' with 'n' elements, find the length of the longest subsequence where a[j]-a[i]=1 given j>i . The order should remain the same.

# In other words, it's longest increasing subsequence were diff between two consecutive element is 1

# Testcase 1:
# a = [2, 3, 1, 4, 3, 5, 6]
# output: 5
# Explanation: the logest subsequence will be [2, 3, 4, 5, 6]

# Update: I solved it using recursion and then optimized to DP, but still got a below average feedback stating "was able to come up with the brute force approach but cldn't optimized it further😢".
# Is there any better optimized solutions for this problem or was I simply out of luck!!
# google
# recursion
# interview
# dp
# google interview question
# recursion+memoization
import collections
arr = [4,1,9,4,5]

dp = {}

ans = 0

for i in range(0,len(arr)):
    if arr[i]-1 in dp:
        ans = max(ans,dp[arr[i]-1]+1)
        dp[arr[i]] = dp[arr[i]-1]+1
    else:
        dp[arr[i]] = 1

print(ans)
