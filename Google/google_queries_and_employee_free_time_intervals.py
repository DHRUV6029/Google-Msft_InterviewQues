# Question 1:
# You are given an array of length n and q queries. Each query consists of two indices [l, r], representing a subarray from index l to r (both inclusive). For each query, we are allowed to subtract 1 from any subsequence within the range [l, r]. After processing all the queries, determine whether it's possible to make all elements of the array equal to zero.

# Example:
# arr = [1, 2, 3]
# queries = [[0, 1], [1, 2], [0, 2], [1, 2]]

# Output: true

# Explanation:
# query --> arr -- subsequence
# [0, 1] --> [0, 1, 3] -- {1, 2}
# [1, 2] --> [0, 0, 2] -- {1 , 3}
# [0, 2] --> [0, 0, 1] -- {2}
# [1, 2] --> [0, 0, 0] -- {1}'


import collections 
mp = collections.defaultdict(int)
arr = [3, 2, 3]   
queries = [[0, 1], [1, 2], [0, 2], [1, 2]]

tmp = [0]*(max(arr)+2)
 

    
for s , e in queries:
    tmp[s]+=1
    tmp[e+1]-=1

for i in range(1,len(tmp)):
    tmp[i] = tmp[i-1]+tmp[i]

for i in range(0,len(arr)):
    if arr[i] == 0 or arr[i] <= 0:
        continue
    if tmp[i] < arr[i]:
        print(False)
        break

print(True)


# You are given a struct Block in C++ that represents the time during which a 
# person is busy, with attributes: personId, startTime, and endTime. 
# You are also given an integer totalTime which represents the total duration. 
# The task is to find the time intervals during which all the persons are free.
import collections
class Person:
    def __init__(self, id, start, end) -> None:
        self.id = id
        self.start = start
        self.end = end


#test suits

p1 = Person(1,2,3)
p2 = Person(2,0,2)
p3 = Person(3,5,6)
p4 = Person(4,9,12)

persons1 = [p1,p2,p3,p4]

p1 = Person(1,2,3)
p2 = Person(2,2,2)
p3 = Person(3,6,6)
p4 = Person(4,9,12)

persons2 = [p1,p2,p3,p4]



def solution(persons):
    mp = collections.defaultdict(int)
    ans = []
    for person in persons:
        mp[person.start]+=1
        mp[person.end+1]-=1
    cur = 0
    start = -1
    li = sorted(mp.items(), key=lambda x : x[0])
    if li[0][0] != 0:
        ans.append((0, li[0][0]-1))
    i = 0 #iteratir pointer
    cur = 0
    while i <len(li):
        cur+=li[i][1]

        if cur == 0:
            if (i+1) < len(li):
                ans.append((li[i][0] , li[i+1][0]-1))
        i+=1



    return(ans)

    
s =  solution(persons2)
print(s)



