# Hi,

# I had this problem last week, and I didn't fully understand it during the interview. I wrote a pseudo-code for the algorithm, and the interviewer confirmed that it was the right solution. It's solved using a binary search algorithm.

# Input: Array of prices of item, and Bundle Limit.
# Output: Find the threshold such as you pay only the bundle limit.

# Example: Array of prices of item: [20, 100, 30, 40, 90] - Bundle Limit: 210
# Result: threshold = 60
# Explanation: items under the threshold are paid with exact price, while items above the threshold are paid with only threshold --> 20 + (100) 60 + 30 + 40 + (90) 60 = 210.

# Has anyone seen this problem before, can explain it to me? I don't quite get the initiative behind it.

arr  =[20, 100, 30, 40, 90]
bundle_limit =  210

l = 0
r = bundle_limit


def canUse(mid):
    ans = 0
    
    for i in range(0, len(arr)):
        if arr[i] > mid:
            ans+=mid
            
        else:
            ans+=arr[i]
            
        if ans > bundle_limit:
            return False
        
    return ans <= bundle_limit

res = 0
while l <= r:
    mid = (r+l)//2
    
    if canUse(mid):
        
        l =mid+1
        res = mid
    else:
        r = mid -1
        
        
print(res)
    