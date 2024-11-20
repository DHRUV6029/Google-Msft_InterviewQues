# arr = [2, 3, 1, 4, 2, 6]
# Answer = 2
# 1 ,2 

# a * 4 = 2 * b

# 2* a = b

# 1*a = 2*b
# Valid quadruplets:
# 1. (2,4,2,4): 2*4 = 2*4 with indices (0,3,4,5)
# 2. (3,2,2,3): 3*2 = 2*3 with indices (1,2,4,5)


# 2 12
# 2 nd condition 
# i , j , k , l

# brute force o(n4) ---> can bring down to o(n2)
# Fix the j and k 

# 4 , 6 -> 24 (now the task is to find l and )

# 4  6 


# a * 4 = 6 * b  --> what will be the ratio (6/4 = b / a)  1.5a = b  ==> serch 
# for b in (k+1:) search for i in (0:j-1)   

# 4 6 (can they occur as j ,k )  ==>    for b in (k+1:) check if 1.5 times a is there No
# 12 4   == ratio 3      

import collections
import copy
arr = [2, 3, 1, 4, 2, 6]

mp_pre = collections.defaultdict(collections.defaultdict)
mp_suf = collections.defaultdict(collections.defaultdict)
ans = 0
for i in range(0,len(arr)):
    if i == 0:
        tmp = collections.defaultdict(int)
        tmp[arr[i]]+=1
        mp_pre[i] = tmp
    else:
        tmpc = copy.deepcopy(mp_pre[i-1])
        tmpc[arr[i]]+=1
        mp_pre[i] = tmpc

for i in range(len(arr)-1, -1 , -1):
    if i == len(arr)-1:
        tmp = collections.defaultdict(int)
        tmp[arr[i]]+=1
        mp_suf[i] = tmp
    else:
        tmpc = copy.deepcopy(mp_suf[i+1])
        tmpc[arr[i]]+=1
        mp_suf[i] = tmpc

#i< j < k < l

def get_i_l(v1 , v2 , i , j):
    ans = 0
    d_l = mp_pre[i-1]
    d_r = mp_suf[j+1]

    r = v1/v2

    for k , v in d_l.items():
        if r*k in d_r:
            ans = ans + (v * d_r[r*k])

    return ans

cnt = 0
for j in range(1 , len(arr)-1):
    
    for k in range(j+1 , len(arr)-1):

        if j != k:

            v = get_i_l(arr[j] , arr[k] , j , k)
            cnt+=v

print(cnt)




    
    
   

   
   

         
            
