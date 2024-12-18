#########################################
#merge k sorted list
arr = arr = [[]]

k = len(arr)
min_heap = []

for i in range(k):
    heapq.heappush(min_heap , (arr[i][0] , i , 0))
ans = []
while min_heap:
    val , r, c = heapq.heappop(min_heap)

    ans.append(val)

    if c + 1 < len(arr[r]):
        heapq.heappush(min_heap , (arr[r][c+1] , r, c+1))


print(ans)

