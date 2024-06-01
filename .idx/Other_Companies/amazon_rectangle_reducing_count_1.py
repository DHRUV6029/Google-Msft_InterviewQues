# Code Question 1
# A student is preparing for a test from Amazon Academy for a scholarship.
# The student is required to completely read n chapters for the test where the ith chapter has pages[i] number of pages. The chapters are read in increasing order of the index. Each day the student can either read till the end of a chapter or at most x pages, whichever is minimum. The number of pages remaining to read decreases by x in the latter case.
# For example, if pages = [5, 3, 4] and x = 4,
# • Day 1: The student reads 4 pages of the first chapter - pages remaining = [1, 3, 4]
# • Day 2: The student can only read till the end of the first chapter - pages remaining = [0, 3, 4]
# • Day 3: The student can read either till the end of the chapter or x = 4 pages, since 3 < 4, the student reads till the end of the chapter 2 - pages remaining = [0, 0, 4]
# • Day 4: The student reads all the 4 pages of the last chapter - pages remaining - [0, 0, 0]
# The test will be given in days number of days from now. Find the minimum number of pages, x, which the student should read each day to finish all pages of all chapters within days number of days. If it is not possible to finish these chapters
# in days number of days, return -1.
# Note: In one day, the student cannot read pages of more than one chapter. Thus, if a chapter finishes, the next chapter starts only on the next day even if the number of pages read is less than x.
# Example
# There are n = 3 chapters, pages = [2, 4, 3], and days = 4.
# Number of pages read each day, x = 3
# 2
# 4
# 3
# After Day 1:
# 0 4 3
# After Day 2:
# 0 1 3
# After Day 3:
# 0 0 3
# After Day 4:
# 0 0 0
# Thus, in 4 days, the student can read all pages of all chapters, and finish. If x is less than 3, it is impossible to read all chapters in 4 days. Thus, the minimum number of pages read each day is 3.
# Function Description
# Complete the function minimumNumberOfPages in the editor below.
# minimumNumberOfPages has the following parameters:
# int pages[n]: the number of pages in each chapter
# int days. the maximum number of days
# Returns
# int: the minimum number of pages to be read each day, or -1 if it is not possible to finish
# Constraints
# • 1≤n≤105
# • 1 ≤ days ≤ 109
# • 1 ≤ pages[i] ≤ 104
# ▾ Input Format For Custom Testing
# The first line contains an integer, n, the number of elements in pages.
# Each line i of the n subsequent lines (where 0 <i<n) contains an integer, pages[i]. The last line contains an integer, days.
# ▼ Sample Case 0
# Sample Input For Custom Testing
# STDIN
# 4
# 2
# 3
# 4
# 5
# 5
# ←
# FUNCTION
# pages[] size n = 4
# pages = [2, 3, 4, 5]
# Sample Output
# days 5
# 4
# import math
# pages = [2,3,4,5]
# x = 4
# l = 0
# r = max(pages)

# ans = float('inf')
# while l <= r:
#     mid = (r+l)//2

#     cnt = 0
#     for i in pages:
#         cnt+=(math.ceil(i/mid))

#     if cnt <= x:
#         ans = min(ans  , cnt)
#         r = mid-1
#     else:
#         l = mid+1
# print(ans)


import heapq
arr = [2, 6, 6, 2, 3, 5]

max_heap = []
ans = 0
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
    c = -heapq.heappop(max_heap)
    d = -heapq.heappop(max_heap)

    #a and b and c and  d are pairs 
    if abs(a-b)<=1 and abs(c-d)<=1:
        ans= ans + (min(a , b) * min(c ,d))

    #if a and b differ by mor ethan 1
    elif abs(a-b)<=1:
        #put them back
        heapq.heappush(max_heap , -a)
        heapq.heappush(max_heap , -b)
    elif abs(c-d)<=1:
        heapq.heappush(max_heap , -c)
        heapq.heappush(max_heap , -d)

        if abs(b-c)<=1:
            heapq.heappush(max_heap , -b)







print(ans)
