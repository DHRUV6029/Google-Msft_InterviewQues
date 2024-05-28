# Maximum area of all possible rectangles that can be formed. The twist here is that you can also reduce any element by atmost 1. find the maximum area of all the rectangles that can be fomed.

# Note: One element can only be used once to form a single rectangle.

# Input1: n = 8 arr[] = [2,3,3,4,6,6,8,8]
# Output: 54
# Explanation: There are two rectangles that can be formed one with edges [6,6,8,8] and another with by reducing 4 by 1 to 3 and reducing 3 by 1 to 2 so the edges will [2,2,3,3]
# Therefore 6 * 8 + 2 * 3 = 54

# Input2: [2,1,6,5,4,4]
# Output: 20
# Explanation: Here just 1 rectangle is possible with maximum by reducing 6 with 5 and hence 5*4 = 20

# Please let me know how we can do this.

import heapq
arr =  [2,2,2,2,2,2,2,2]

max_heap = []
area = 0
for i in range(0 ,len(arr)):
    heapq.heappush(max_heap , -arr[i])

def reduce_element_condition(a , b):
    if a > b and a - b == 1:
        return True
    return False

while len(max_heap)>=4:
    #need to pick 4 values 
    a = -heapq.heappop(max_heap)
    b = -heapq.heappop(max_heap)

    if a!=b and reduce_element_condition(a , b):
        a = a-1
      
    c = -heapq.heappop(max_heap)
    d = -heapq.heappop(max_heap)

    if c!=d and reduce_element_condition(c , d):
        c-=1

    if a==b and c==d:


        area+=a*c

print(area)




