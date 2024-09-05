# Hi everyone,

# I tackled a couple of interesting problems from an Amazon Online Assessment (OA) and wanted to share them with you. Below are the detailed problem descriptions along with the class declarations for each problem. These tasks are great for practicing array manipulation and queue simulations.

# Problem 1: Reduce Gifts

# Task Description:

# Amazon is having a sale, and you have a list of item prices.
# To ensure the sum of prices for any k items does not exceed a 
# \specified threshold,
# you need to determine the minimum number of items to remove from the list.

# Given:
# An array of integers prices representing the prices of each item.
# An integer k, which is the number of items to consider for the sum.
# An integer threshold, which is the maximum allowed sum for any k items.

# Objective:
# Find the minimum number of items to remove so that the sum of prices of any k items does not exceed the threshold.

# Example:
# public class Solution {
#     public static int reduceGifts(List<Integer> prices, int k, int threshold) {
#         // Implementation here
#     }
# }
# Example Input:
# prices = [9, 6, 7, 2, 7, 2]
# k = 2
# threshold = 13
# k-pairs should be less than threshold , k pairs do not form a subarray 
# #approach 
# seed the max_heap with all the numbers
# now pop out k elements from it (it will be largest two if they exceed the thresold remocve them)
# do this untill sum of k elemnt window is less than eqaiul to threshod,


import heapq

prices = [9, 6, 7, 2, 7, 2]
k =2
threshold = 13
max_heap = []

for i in range(0,len(prices)):
    heapq.heappush(max_heap, (-prices[i]))

cnt = 0
while True:
    s = 0
    for _ in range(k):
        s+=(-heapq.heappop(max_heap))

    if s > threshold:
        cnt+=k
    else:
        break

print(cnt)



