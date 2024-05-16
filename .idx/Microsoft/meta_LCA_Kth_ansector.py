# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

# The kth ancestor of a tree node is the kth node in the path from that node to the root node.

# Implement the TreeAncestor class:

# TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
# int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.
#Extending the algorithm to find the many LCAs
import math
import collections
parent =[-1, 0, 0, 1, 1, 2, 2]
n = 7

depth = [-1] * n

mp = collections.defaultdict(list)

for i in range(0,len(parent)):
    mp[parent[i]].append(i)


###################################Finding Levels of each node##########################
#O(n)
def find_levels(node, ancestor):
    depth[node] = depth[ancestor]+1

    for ch in mp[node]:
        if mp[ch] != -1:
            find_levels(ch, node)
find_levels(0 , -1)
###################################Finding Levels of each node##########################


###################################Building sparse Matrix###############################
#0(n*m). m = log(n)
m = max(depth)+1 #levels in binary tree
dp = [[-1 for i in range(m)] for j in range(n)]


for j in range(m):
    for i in range(n):
        if j == 0:
            dp[i][0] = parent[i]
        elif dp[i][j-1]!=-1:
            dp[i][j] = dp[dp[i][j-1]][j-1]
###################################Building sparse Matrix###############################


def find_lca(u, v):
    #need to match the depth of u and v
    node = None
    k = 0
    
    if depth[u] > depth[v]:
        node = u
        k = depth[u] - depth[v]
        
        u = binary_lift(k, node )
            
    elif depth[v] > depth[u]:
        node = v
        k = depth[v] - depth[u]
        
        v = binary_lift(k, node )
    
    if u == v:
        return u
    
    for i in range(0, m-1):

        if dp[u][i] == -1 or dp[v][i] == -1:
            continue
        
        if  dp[u][i] == dp[v][i]:
            return dp[u][i]
            

    return -1




def binary_lift(k, node):
    for i in range(m-1, -1, -1):
        if (k & (1 << i)) ==1:
            node = dp[node][i]

    return node



print(find_lca(1,2))






    


    











