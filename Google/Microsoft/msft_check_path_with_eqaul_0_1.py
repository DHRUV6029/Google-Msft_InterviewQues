# There are n coins and m people. we have to make m combinations from these n coins such that sum of each combination is minimum. we can use any coin any no. of times and each combination should have different sum. now print the sum of all combinations we made.
# Test case:
# n=3,m=5
# arr=[3,5,11]
# person1: 3
# person2: 5
# person3:3+3
# person4:3+5
# person5:3+3+3
# Sum=31.
# First M combinations with smallest sum.
import heapq


arr =[1,2,3]
n=3
m=6
arr.sort()
minHeap = []

for i in arr:
    heapq.heappush(minHeap , (i, [i]))

seen_set = set()
ans = 0
for _ in range(0,m):
    cur_sum , cur_comb = heapq.heappop(minHeap)
    ans+=cur_sum
    seen_set.add((cur_sum , tuple(cur_comb)))

    for i in arr:
        cur_sum += i
        cur_comb.append(i)
        if (cur_sum , tuple(cur_comb)) not in seen_set:
            
            heapq.heappush(minHeap , (cur_sum , cur_comb))
        

print(ans)
        
        
        