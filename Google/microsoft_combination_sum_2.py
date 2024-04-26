A = [2,2,3]
target = 5

n = len(A)
res =[]
path =[]
def backtrack(i , remain):
    
    if remain == 0:
        res.append(path.copy())
        
    if remain < 0:
        return
    
    
    for j in range(i , n):
        if j > i and A[j] == A[j-1]:
            continue
        path.append(A[j])
        backtrack(j, remain-A[j])
        path.pop()
        
        
A.sort()
backtrack(0, 5)
print(res)
        