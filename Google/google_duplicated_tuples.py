# Given n edges
# Each edge has 3 patterns like below :

# e1 -> p1, p2, p3
# e2 -> p1, p5, p3
# e3 -> p2, p5, p1
# e4 -> p3, p5, p6

# An edge is said to be duplicate of another edge if they have any one common pattern. Return the list of duplicated edges.
# output = {e1, e2, e3},{e1, e2, e4}, {e2,e3, e4}
import collections

input = {
    'e1' : [1, 2, 3],
    'e2' : [1 , 5 , 3],
    'e3' : [2,5, 1],
    'e4' : [3,5,6]
}


#assumption we know the max bit val n = 6
n = 6
res = []

bit_map = collections.defaultdict(int)


for k , v in input.items():
    bitmask = 0
    for i in v:
        bitmask = bitmask | (1 << i)
        
    bit_map[k] = bitmask
    
for k1, v1 in bit_map.items():
    cur_mask = v1
    tmp = [k1]
    for k2,v2 in bit_map.items():
        
        if k1 != k2:
            if cur_mask & v2 != 0:
                tmp.append(k2)
                cur_mask = cur_mask | v2
            
            
                
    res.append(tmp)
    
print(res)