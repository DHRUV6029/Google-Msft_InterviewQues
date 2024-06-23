# Hi folks, recently I had an interview with "MAANG" where I was asked this following question. I could come up with a brute force solution but not the best solution.

# Question:

# A kid found out that his uncle loves him so much that he would do anything to buy him as many gifts as he possibly can. For this reason, the nephew prepares a list of gifts that he wants and gives it to his uncle. Each item in the list contains 2 integers: the day on which he wants the gift (today is day 0), and the cost of it. The uncle, knowing that his nephew is preparing such a list, saves $1 per day for the gifts, and initially (on day 0) he has $0. Calculate the maximum number of gifts the uncle can buy to his nephew.

# Input: The first line contains a single integer N - the number of gifts. Then N lines follow. Each line contains two integers separated by space: d_i (the day that present i should be bought) and c_i (the cost of gift i).

# Output: A single integer which is the maximum number of gifts the uncle can buy.
import heapq
arr = [[1,2],[3,2],[5,3],[6,2],[7,2]]


maxHeap = []
ans = 0
money = 0
for i in range(0,len(arr)):
    if i == 0:
        money = arr[i][0]
    else:
        money+=(arr[i][0]-arr[i-1][0])  #assuming days will be in sorted order
    
    if money >= arr[i][1]:
        heapq.heappush(maxHeap , -(arr[i][1]))
        ans+=1
        money-=arr[i][1]
    else:
        while maxHeap and money<0:
            money+=(-heapq.heappop(maxHeap))

print(ans)
