import collections
import bisect
# arr = [1,2,4,5,6]


# # find all pairs such that (arr[i] - arr[j] == i -j)
# # possible pairs here  (2,1) (4,5) (4,6) (5,6)  ==> 4 pairs
# #arr[i]- i == arr[j] - j

# cnt = 0
# mp = collections.defaultdict(int)

# for i in range(0,len(arr)):
#     val = arr[i] - i

#     if val in mp:
#         cnt = cnt + mp[val]

#     mp[val]+=1

# print(cnt)

# #approach 

#Lenght of longest increasing subsequcne with difference between adjacent elemets is <=D

#Binary search approach

arr = [1,2,6,7,8,1,9]

k =2
subs= []

for i in range(0 , len(arr)):
    idx = bisect.bisect_left(subs , arr[i] , key=lambda x : x[0])
    if not subs:
        subs.append((arr[i],i))
        continue
    if idx == len(subs) and abs(subs[-1][1] - i) <= k:
        subs.append((arr[i], i))

    else:
        
        if abs(subs[idx-1][1] - i) <= k:
            subs[idx] = (arr[i], i)

print("test")

