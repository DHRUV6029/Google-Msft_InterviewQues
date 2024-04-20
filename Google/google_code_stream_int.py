# Find triplets from this incoming stream such that difference between the elements in pair is at most targ
# targ=7
# stream=22,3,1,8,10,6,13,.......
# op=[(3, 1, 8), (3, 1, 6), (3, 8, 10), (3, 8, 6), (3, 10, 6), (1, 8, 6), (8, 10, 6), (8, 10, 13), (8, 6, 13), (10, 6, 13)]

# Since the approach is extremely costly, the interviewer was unhappy with the approach so I couldn't move to the next round. Someone please help me with the optimal approach to this questio

#Questions to ask 

#Does the order matter (of tuples, or not) -> If yes than Binary search with sorted array will work else 
#not
#Assuming it is a incommming stream the order mattwers in realiric secanrop

import collections
cnt = collections.Counter()
pairs = collections.Counter()
stream=[22,3,1,8,10,6,13]
target = 7

res = set()
for i in stream:
    #span of i or search space or i - target to i + target
    for j in range(i- target , i+target+1):
        
        #for j th elemnet again the search space in j + target but lesser than i
        
        for k in range(j ,min(i, j)+target+1):
            
            res|={(j, k ,i)*pairs[j, k] , (k ,j ,i)*pairs[k, j]}
            
        #here we all have pairs possibel with i as last elemebt
        pairs[j , i]|=cnt[j]
        
    cnt[i] = 1
    
print(res - {tuple()} )
        
