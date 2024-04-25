# Given an input array, find the largest sum of a subset that doesn’t contain neighboring values. A neighboring value is defined as this: for number n, value n-1, n+1 are its neighboring values. For example, 2 is the neighboring value of 1, 3. 
# For example, given input {1,1,2,2,2,3,3,3,6}, the largest subset that doesn’t contain neighboring values is {1,1,3,3,3,6}, and sum is 17.



#we also need the subset as weel  how to get it maybe DP array helps??????
#No bcoz dp arrayt captures only the max value not the used actual choices

import collections
arr = [1,2,3,7,8,6,7,6] #assumning this is sorted 

cnt = collections.Counter(arr)
mp = collections.defaultdict(int)
for i in range(0,len(arr)):
    mp[arr[i]]+=arr[i]
    
    
dp = [0]*(max(arr)+1)
subset = [0]*(max(arr)+1)
#init the dp 

dp[1] = mp[1]   
subset[1] = 1
ans= 0
for i in range(2,len(dp)):
    #goal is to maxi,ize the value 
    #choice 1 -> take this cant take the previous one
    #choice 2 -> not take this ans is precdeing value
    take_this  = dp[i-2]+mp[i]
    not_take_this = dp[i-1]
    

    if take_this >= not_take_this:
        subset[i-1] = 0
        subset[i] = 1
    else:
        subset[i] = 1
   
    dp[i] = max(dp[i-1] , dp[i-2]+mp[i])
    
ans = []
for i in range(0,len(subset)):
    if subset[i] == 1:
        ans.extend([i]*cnt[i])
        
print(ans)
    
    
    


