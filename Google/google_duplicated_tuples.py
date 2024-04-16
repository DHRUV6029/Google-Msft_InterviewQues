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


for every pattern in every edge,

hashMap = defaultdict(list)
for edge in edges:
    for pattern in edge:
        hashMap[pattern].append(edge)
now we have:
{
p1: [e1, e2, e3]
p2: [e1, e3]
p3: [e1, e2, e4]
p4: []
p5: [e2, e3, e4]
p6: [e4]
}

for pattern, edges in hashMap.items()
    if len(edges) > 1:
        res.append(edges)
answer would be:
[
[e1, e2, e3],
[e1, e3],
[e1, e2, e4],
[e2, e3, e4]
]

is this correct?

time: O(e * p + p)
space: O(p * e) (?) because we have p patterns which each store e edges they're related to. Not sure about this
e = edges
p = patterns