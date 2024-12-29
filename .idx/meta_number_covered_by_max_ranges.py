import collections

# You are given n bounded integer intervals [[start1, end1], [start2, end2]; determine any point that belongs to the maximum number of intervals.
# [1, 5] [2, 4] [3, 13] [6, 10] [10, 12] [11, 13];
# Expected: 3 or 10, because 3 is in 1-5, 2-4, 3-13 3 times.


#If the intervals are sorted we can use dict approeach for a NlogN Tc solution
intervals = [[1, 5], [2, 4] ,[3, 13] ,[6, 10], [10, 12] ,[11, 13]]


mp = collections.defaultdict(int)

for i in range(0,len(intervals)):
    mp[intervals[i][0]]+=1
    mp[intervals[i][1]+1]-=1


ans = -1
cur_max = 0
cur_sum =0
for k , v in sorted(mp.items()):
    cur_sum+=v

    if cur_sum > cur_max:
        cur_max = cur_sum
        ans = k

print(ans)

