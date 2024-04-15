# -> Remove all duplicate messages that occur within 10 seconds

# Question - There's an input stream where you receive messages from another system. The frequency of messages is pretty high such that your system would not handle such huge amount of message processing.

# Task to achieve - Duplicate messages should be completely removed from the output if they occur within 10 seconds.

# Input:
# 10 Message A
# 11 Message B
# 12 Message C
# 13 Message A
# 14 Message B
# 21 Message A
# 35 Message A

# Output:
# 12 Message C
# 35 Message A

import collections
import bisect

input = ['10 Message A' ,'11 Message B' ,'21 Message C','21 Message A','14 Message B','26 Message A','35 Message A']

#Approach Use Binary Search to covder the range

mp = collections.defaultdict(list)
cur_time = 0


for msg in input:
    _ts = msg.split(' ')[0]
    _id  = msg.split(' ')[2]
    mp[_id].append(int(_ts)) 
    
    
def get_exclusive_ts(arr):
    hset = set()
    for i in range(0, len(arr)):
        idx = bisect.bisect_left(arr , arr[i]+10)
        if abs(idx - i)>1:
            for j in range(i , idx):
                hset.add(arr[j])
                
    return hset


def print_exclusive_ts(to_remove , k, v):
    for i in v:
        if i not in to_remove:
            print(str(k) + " message " + str(i))
           
            
            
for mesg , ts in mp.items():
    to_remove = get_exclusive_ts(ts)
    print_exclusive_ts(to_remove , mesg , ts)
    
    
    
       
        

            

