# my interview question is to find minimum positive 
# difference between 2 elements 
# in an array but in O(N) how can i do it.

arr = [1,2,3,4,5,6,7]

buckets = [0]*max(arr)

for i in range(0,len(arr)):
    buckets[arr[i]-1] = 1

last = None
diff = float('inf')

for i in range(0,len(buckets)):
    if buckets[i] > 0:
        if last is not None:
            diff = min(diff, abs(i-last))
        last = i

print(diff)

