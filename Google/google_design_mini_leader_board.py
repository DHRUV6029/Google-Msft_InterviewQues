# Design a mini leaderboard. It should have the following methods.

# insert(uid) - inserts a new user id into the mini leaderboard
# update(uid, score) - updates the score of the given user id with score
# topk() - returns top k userids and their scores
# getWindow(uid, k) - return k userids around the given uid. Preferrably, the given uid can be placed in the middle if possible.

# #REQUIREMENTS
# 1. -> hashmap to maintain uid-> score
# 2. -> Updates happen to hashmap
# 3. -> topk (based on scores)-> priorty queue  [Stale set to do lazy deletion]
# 4. -> to keep a window (surronding uids , assuming uids are integers we can maintain a sorted container,
#                         that stores all the uids in sorted manner then we binary search and find
#                         k//2 on left and k//2 on right (will not be always possible)).
# TC ----> Analysis
# 1. insert -> O(1)
# 2. updates -> O(1)
# 3. topk -> O(klogn)
# 4. getwindow O(nlogn)

import collections
import heapq
import bisect
class LeaderBoard:
    def __init__(self) -> None:
        self.map = collections.defaultdict(int)
        self.stale = set()
        self.maxHeap = []
        
        
    def insert(self , uid):  #work done create new entries in hamp and 
        self.map[uid] = 0 #will not feature in topk

        
    def update(self , uid, score):
        old_score = self.map[uid]
        if old_score > 0:
            self.stale.add((-old_score  , uid))
        self.map[uid]+=score
        heapq.heappush(self.maxHeap , (-self.map[uid] , uid))
        
    def topk(self, k):
        res = []
        while k and self.maxHeap:
            cur = heapq.heappop(self.maxHeap)
            if cur in self.stale:
                self.stale.remove(cur)
            else:
                res.append((-cur[0], cur[1]))
                k-=1
                
        return res
                
    def getwindow(self ,uid,  k):
        uids = list(self.map.keys())
        uids.sort()
        
        i = bisect.bisect_right(uids ,uid)
        left_offset = min(k // 2+1, i)
        right_offset = min(k // 2+1, len(uids) - i - 1)
        start = i - left_offset
        end = i + right_offset 
        return uids[start:end]

        
    
l = LeaderBoard()
l.insert(1)
l.update(1, 4)

l.insert(3)
l.update(3, 4)

l.insert(2)
l.update(2, 5)

l.insert(4)
l.update(4, 4)

l.insert(5)
l.update(5, 9)


l.insert(8)
l.update(8, 19)
l.update(8, 12)

print(l.topk(3))

print(l.getwindow(3 , 4))


        
        
        
                
                
                
        
        
        
        
        
