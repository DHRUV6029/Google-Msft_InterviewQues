# 3. Design a search data structure to store and display recent searches. If
# a user just clicks the search bar without typing anything, it should
# return the N most recent searches. Given a search string it should save
# the search and also return the N most recent searches

import heapq
import collections

stale = set()
search_dict = []
map = collections.defaultdict(int)
def getSearchStrinds(word ,N):
    if word == '':
        #simulating user click
        print(topNSearches(N))
    else:
        if word in map:
            stale.add((-map[word] , word))
        map[word]+=1
        heapq.heappush(search_dict , (-map[word], word))
        print(topNSearches(N))
        
        
        
def topNSearches(n):
    res = []
    i = 0
    while n and len(search_dict)>= n:
        if search_dict[i] in stale:
            stale.remove(search_dict[i])
            heapq.heappop(search_dict)
            
        else:
            res.append(search_dict[i][1])
            n-=1
            i+=1
            
    return res
    
    
getSearchStrinds("test",2)
getSearchStrinds("test1",2)
getSearchStrinds("test2",2)
getSearchStrinds("test",2)
getSearchStrinds("test",2)
getSearchStrinds("test",2)
getSearchStrinds("test",2)
getSearchStrinds("")
        
        
    
