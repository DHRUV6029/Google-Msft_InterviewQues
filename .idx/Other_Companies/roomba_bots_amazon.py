def solution(x, y):
    n = len(x)
    
    maxX = {}
    maxY = {}
    minX = {}
    minY = {}

    for i in range(n):
        if x[i] > maxX.get(y[i], float('-inf')):
            maxX[y[i]] = x[i]
        if x[i] < minX.get(y[i], float('inf')):
            minX[y[i]] = x[i]
        if y[i] > maxY.get(x[i], float('-inf')):
            maxY[x[i]] = y[i]
        if y[i] < minY.get(x[i], float('inf')):
            minY[x[i]] = y[i]

    result = 0

    for i in range(n):
        if (
            x[i] != maxX.get(y[i])
            and x[i] != minX.get(y[i])
            and y[i] != maxY.get(x[i])
            and y[i] != minY.get(x[i])
        ):
            result += 1
    
    return result

print(solution(
    [0,0,0,0,0,1,1,1,2,-1,-1,-2,-1],
    [-1,0,1,2,-2,0,1,-1,0,1,-1,0,0]
))  # Output: 2


