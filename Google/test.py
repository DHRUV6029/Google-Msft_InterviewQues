import bisect
arr = [1,3,5,5,6]

idx = bisect.bisect_left(arr ,4)
print(idx)
