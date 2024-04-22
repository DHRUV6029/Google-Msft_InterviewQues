# # given 2 circles with their centres and radius, return true if they are intersecting or false if they are not

# # i've misunderstood the question as given n circles so wasted half of the time, later made clear its only 2 circles and the distance to calculate between two points was given d=√((x2 – x1)² + (y2 – y1)²)


# https://leetcode.com/problems/maximum-path-quality-of-a-graph/description/

# You have a graph, where each node is a bank with $X in the vault, and each edge between the banks represents the time it takes to travel between the banks. You're a bank robber and you start by robbing bank 0. Given time limit T, what is the maximum amount of money you can rob across all the banks if you must end at bank 0 because that's where your getaway car is.

# I proposed Djikstra to minimize the travel time, but couldn't figure out how add the part to maximize the money robbed. Maybe there's some DP component too?

# Edit: Graph is undirected, and you can revisit the same bank as part of your path to get back to 0, but you can't rob it more than once.

import collections

stream=[22,3,1,8,10,6,13]
one,two= collections.Counter(),collections.Counter()
res=set()
for i in stream:     
    for j in range(i-7,i+8):
        for k in range(j,min(i,j)+8):
            res|={(j,k,i)*two[j,k], (k,j,i)*two[k,j]}              
        two[j,i]|=one[j]       
    one[i]=1

print(res-{tuple()})