# Given an array A with only positive numbers. We are allowed to negate any entries in the array, (i.e set A[i] = -A[i]). What is the maximum number of entries you can negate in the array such that every prefix sum after the negate operations is positive.

# Example 1:

# Input: A = [4, 1, 1, 1]
# Output: 3
# Explanation:

# We can apply only at-most 3 negate operations, to make A = [4, -1, -1, -1], after the negate operation,

# The prefix sums of A, p(A) = [4, 3, 2, 1] which are all positive. So that the answer for A is 3.

import heapq
A = [4, 1, 1, 1]
maxHeap = []
cur_sum = A[0]

#CANNOT negate the first element
ans = 0
for i in range(1 , len(A)):
    if cur_sum > A[i]:
        cur_sum-=A[i]
        heapq.heappush(maxHeap , -A[i])
        ans+=1
    elif maxHeap and -maxHeap[0] > A[i]:
        val = -heapq.heappop(maxHeap)
        cur_sum+= (2*val - A[i])
        heapq.heappush(maxHeap , -A[i])
    else:
        cur_sum+=A[i]
        
print(ans)
