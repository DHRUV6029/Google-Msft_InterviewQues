# You and a friend have received a special gold chain as a gift.
# The chain links each have an integer weight, not necessarily the same
# You and your friend must choose one of the links to be removed and provided to charity,
# after which the chain will be reconnected. After that, you can choose one place along the chain to split it in two,
# such that it creates two equally-weighted sections for you and your friend to take home.
# For a given input chain (list of link weights), determine if a solution is possible.

import bisect
arr = [1,2,8]


prefix = [arr[0]]
suffix = [arr[-1]]

for i in range(1,len(arr)):
    prefix.append(prefix[-1]+ arr[i])
    
for j in range(len(arr)-2, -1, -1):
    suffix.append(suffix[-1]+arr[j])
    
prefix.append(0)
prefix.insert(0,0)

suffix.append(0)
suffix.insert(0,0)

rev_suffix= suffix[::-1]


for i in range(1 , len(prefix)-1):
    if suffix[i]==prefix[i] and i != len(prefix)-2:
        print(True)
        break
    
    else:
        diff = prefix[i] - suffix[i]
        if diff % 2 ==0:
            
            #if diff > 0 means suffix needs to pass somrhing to prefix 
            if diff > 0:
                need = diff//2
                idx = bisect.bisect_left(rev_suffix[i:] , suffix[i]+need)
                if suffix[idx] == suffix[i]+need:
                    print(True)
                    break
            else:
                need = diff//2
                idx = bisect.bisect_left(prefix[:i+1] ,prefix[i]-need)
                if prefix[idx] == prefix[i]+need:
                    print(True)
                    break
                
print(False)                
            
        



        
        
    
    