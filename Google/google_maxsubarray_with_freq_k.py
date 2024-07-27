# The organizers of a gaming tournament want to analyze player participation based on event logs. There are n event logs, where arr[i] indicates the playerId of the player who participated in the ith event. The organizers need to identify subarrays of these logs that are consistent, meaning that the frequency of the most frequent player in the subarray matches the frequency of the least frequent player in the entire array. Determine the maximum length of such consistent logs.

# Example
# Given:

# n = 10

# arr = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]

# The frequencies of playerIds 1 and 2 are 2.

# The frequencies of playerIds 3 and 4 are 3.

# The minimum frequency in the array is 2.
# The longest valid subarray with this property is [1, 2, 1, 3, 4, 2, 4, 3], which has 8 elements. In this subarray, the most common element appears 2 times, which matches the minimum frequency in the entire array. Therefore, the maximum length of consistent logs is 8.

# Function Description
# Complete the function findConsistentLogs with the following parameters:

# int arr[n]: the playerIds present in the event logs
# Returns
# int: the maximum length of the consistent logs
# Constraints
# 1<= n <=10^4
# Can someone please help with the approach and solution of this problem?

# google
# google online challenge
# google coding challenge

import collections
arr = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]

k = float('inf')

count = collections.defaultdict(int)

for i in range(0,len(arr)):
    count[arr[i]]+=1

for ki , v in count.items():
    k = min(v , k)

l = 0
max_len = float('-inf')
mp = collections.defaultdict(int)
for r in range(0,len(arr)):
    mp[arr[r]]+=1

    if mp[arr[r]] >k:
        while l < r and mp and mp[arr[r]] > k:
            mp[arr[l]]-=1

            if not mp[arr[l]]:
                mp.pop(arr[l])

            l+=1

    max_len = max(max_len , r-l+1)

print(max_len)


