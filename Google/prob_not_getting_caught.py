# There is a class room where students sit in a fashion that resembles matrix. 
# In a class students wants to pass notes around without getting cought by the teacher. 
# The probability of getting caught by teacher decreases as we move further away to 
# teacher by half and probability of getting caught remains same in the same row. 
# Given an NxN matrix with starting point and final point return the minimum probability 
# of getting caught.


import heapq

matrix = [[]]
m = len(matrix)
n = len(matrix[0])

dp = [[float('inf') for _ in range(n)] for _ in range(m)]

direc = [(0,1),(0,-1),(-1,0),(0,-1)]

src  = [(0, 0)]
dest = [(2,4)]

dp[0][0] = 0 # min probabliity
min_heap = [(0, (src[0], src[1]))]

while min_heap:
    cur, x, y = heapq.heappop(min_heap)

    #exit condition
    if x == dest[0] and y == dest[1]:
        print(cur)
        break

    for dr ,dc in direc:
        nr , nc = x+dr, y+dc

        #check out of boubds condition
        if nr < 0 or nc < 0 or nr > m-1 or nc > n-1:
            continue

        #if same row probablility diesnt changes, it only changes with  col

        if nr !=x and nc == y:
            cur = cur - (matrix[nr][nc]/2)

        if dp[nr][nc] > cur:
            dp[nr][nc] = cur
            heapq.heappush(min_heap , (cur , (nr , nc)))









