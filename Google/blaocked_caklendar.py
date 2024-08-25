# The given problem was -

# Given a calendar of N people.

# Calendar is marked as Blocked if person is not available (both days inclusive)

# Return number of days when all are available in given D days.

# person 1 - [2,3], [9,10]
# person 2 - [4,5]
# person 3 - [7,9]

# D = 10

# output = 2 (1, 6)

# Follow up : Return number of days when at least P people are available.
# Ans



import collections
calendar  = {
    'person 1' : [[2,4], [9,10]],
    'person 2' : [[4,5]],
    'person 3' : [[7,9]]
}

D = 10

arr = [0]*(D+2)

for k , v in calendar.items():
    for s,e in v:
        arr[s]+=1
        arr[e+1]-=1

cnt = 0
days = []

cur = 0
for i in range(1, min(D, len(arr))):
    cur = cur + arr[i]

    if cur == 0:
        cnt+=1
        days.append(i)

print(cnt)
print(days)


#############Follow Up code#################

P =2
days = []
idx = collections.defaultdict(set)

for k , v in calendar.items():
    for s,e in v:
        idx[s].add(k)
        idx[e+1].add(k)

idx = dict(sorted(idx.items(), key=lambda x : x[0]))

active_set = set()

for k, v in idx.items():
    for p in v:
        if p in active_set:
            active_set.remove(p)
        else:
            active_set.add(p)

    if len(active_set) >= P:
        days.append(k)

print(days)


