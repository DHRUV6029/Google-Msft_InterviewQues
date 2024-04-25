# There is a stream of integers. Every time you see a new element in the stream, return the mean value of the last N elements, excluding the largest K elements.

# Example:
# N = 5
# K = 2
# elements so far = [20, 2, -2, 0, 10, 1, 5, -2, 0]

# last N elements: [10, 1, 5, -2, 0]
# largest K elements: [10, 5]
# result = (1+(-2)+0)/3 = -0.3333333

# I could not find a neat approach but only a suboptimal one.

import collections
import heapq
maxHeap = []
N = 5
K =2
nums = [20, 2, -2, 0, 10, 1, 5, -2, 0]
left = 0
right = 0

k =K
cur_sum = 0
ans = []
#process first k elements
for i in range(0,N):
    cur_sum+=nums[i]
    heapq.heappush(maxHeap , (-nums[i], i))
    
k_max = 0
i = 0
while k and i <len(maxHeap):
    k_max-=maxHeap[i][0]
    k-=1
    i+=1

ans.append((cur_sum-k_max)//(N-K))

l = 0
for i in range(N ,len(nums)):
    cur_sum+=nums[i]
    cur_sum-=nums[l]
    l+=1
    heapq.heappush(maxHeap , (-nums[i], i))
    
    k_max = 0
    k = K
    
    tmp_store = []
    while k and maxHeap:
        if l <= maxHeap[0][1] <= i:
            k_max-=maxHeap[0][0]
            tmp_store.append(heapq.heappop(maxHeap))
            k-=1
        else:
            heapq.heappop(maxHeap)
            
            
    ans.append((cur_sum-k_max)/(N-K))
    
    while tmp_store:
        heapq.heappush(maxHeap, tmp_store.pop())
        
print(ans)
            
    
            
            
        
        

    
    
    
    