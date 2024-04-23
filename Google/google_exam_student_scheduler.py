# A number of students are taking exams in a room. Students sitting adjacent to each other and taking the same exam can cheat. Arrange the students so that cheating opportunities are minimized. I was free to choose input format.
# I chose the input to be a list of length n, denoting n students. The element at index i would indicate the exam student i is taking.
# For example, [1,2,3,1,2,2]
# Student 0 is taking exam 1
# Student 1 is taking exam 2
# Student 2 is taking exam 3
# Student 3 is taking exam 1
# Student 4 is taking exam 2
# Student 5 is taking exam 2
# Output would be a list with the students re-arranged. An acceptable output for the above case would be [1,2,3,2,1,2].
import collections
import heapq

arr = [5,4,4,4,1,4]

space = 2
cnt = {}
ans = []
for i in range(0 ,len(arr)):
    cnt[arr[i]] = cnt.get(arr[i],0)+1
    
minHeap=[]

for k ,v in cnt.items():
    heapq.heappush(minHeap , (-v , k))
    
while heapq:
    cycle =space
    store = []
    while cycle and minHeap:
        cnt , val = heapq.heappop(minHeap)
        cnt = abs(cnt)
        cycle-=1
        ans.append(val)
        cnt-=1
        
        if cnt > 0:
            store.append((-cnt , val))
            
    while store:
        heapq.heappush(minHeap , store.pop())
    
    if len(ans) == len(arr):
        print(ans)
        break
    
    
print(ans)
    
    
        




