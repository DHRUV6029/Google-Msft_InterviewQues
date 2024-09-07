# Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution

# A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.

# For example,
# A: [1,5], [10,14], [16,18]
# B: [2,6], [8,10], [11,20]

# output [1,6], [8, 20]

A  =[[1,5], [10,14], [16,18]]
B = [[2,6], [8,10], [11,20]]

i , j = 0 , 0

cur = None
res = []
while i < len(A) or j < len(B):

    #case-1 i == len(A) increment the other 
    if i >= len(A):
        cur = B[j] 
        j+=1
    elif j == len(B):
        cur = A[i]
        i+=1
    elif A[i][0] < B[j][0]:
        cur =  A[i]
        i+=1
    else:
        cur = B[j]
        j+=1

    if res and res[-1][-1] >= cur[0]:
        res[-1][-1] = max(res[-1][-1], cur[-1])
    else:
        res.append(cur)

print(res)



