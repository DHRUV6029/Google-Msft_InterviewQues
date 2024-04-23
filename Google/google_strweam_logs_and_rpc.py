# You have a stream of rpc requests coming in. Each log is of the
# form {id, timestamp, type(start/end)}. Given a timeout T, you need to figure out at the earliest possible time if a request
# has timed out.
# Eg :
# id - time - type
# 0 - 0 - Start
# 1 - 1 - Start
# 0 - 2 - End
# 2 - 6 - Start
# 1 - 7 - End
# Timeout = 3
# Ans : {1, 6} ( figured out id 1 had timed out at time 6 )
import collections
import heapq
stream_logs = [(0  , 0 , 'Start') , (1  , 1, 'Start') , (0 , 2 , 'End') , (2 , 6 ,'Start') ,(1,7,'End')]
T = 3
mp = collections.defaultdict(int)
minHeap = []


def check_time_out(t):
    res= []
    while minHeap[0][0] < t:
        
        cur = heapq.heappop(minHeap)
        if  cur[1] in mp:
            res.append((cur[1] , t))
            mp.pop(cur[1])
            
    return res
        


for _id , t , _type in stream_logs:
    if _type == 'Start':
        mp[_id] = t+T
        heapq.heappush(minHeap , (t+T , _id))
        check_time_out(t)
    else:
        # 
        #this is the end 
        if _id in mp:
            #this will not be timed out 
            if mp[_id] > t:
                mp.pop(_id)
        
        check_time_out(t)    
        
        
       
        
        

