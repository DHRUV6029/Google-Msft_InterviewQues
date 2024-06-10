errorString = "101!1"

x = 2
y = 3


dp = {}
def solve(i , zero , one):
    if i == len(errorString):
        return 0

    if (i , zero ,  one) in dp:
        return dp[(i , zero , one)]

    ans = float('inf')

    if errorString[i] == '0':
        ans = min(ans , solve(i+1 , zero+1 , one) + y * one)
    elif errorString[i] == '1':
        ans = min(ans , solve(i+1 , zero , one+1) + x * zero)
    else:
        with_zero = solve(i+1,zero+1,one) + (y*one)
        with_one  = solve(i+1 , zero , one+1) + (x*zero)
        ans = min(with_zero , with_one)

    dp[(i , zero , one)] = ans
    return ans


res = solve(0, 0, 0)
print(res)

    
