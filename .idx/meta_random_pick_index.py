# Definition for a binary tree node.
import random
from typing import List , Optional
from collections import Counter, defaultdict , deque
import heapq
#########################################   
# Definition for a binary tree node.
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        self.total = 0

        for i in range(1,len(self.w)):
            self.prefix.append(self.prefix[-1]+w[i])

        self.total = self.prefix[-1]

        

    def pickIndex(self) -> int:
        target = self.total * random.random()  #generate value with 1 digit desimal 
        #precision 

        l, r = 0 ,len(self.prefix)-1

        while l <= r:
            mid = (r+l)//2

            if self.prefix[mid] < target:
                l = mid+1
            else:
                r = mid-1

        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# [1,3,4]
#Approach-1 Resorivoir Sampling with value to index mapping 

# [1,3,3,3,4,4,4,4]  ---> now if you pick random 
# index = 1 (1/8)-> 12.5
# index = 3 (3/8) -> 37.5


#Approach-2 (Prefix sum with binary seerch )
# 1,4,8 -> prefix sum

# 1-> [0,1) 1      12.5
# 3->[1,4)  3      37.5
# 4-> [4,8)  4     50
        
# why run sum woks each number gets range prop to its value/weight 



        




