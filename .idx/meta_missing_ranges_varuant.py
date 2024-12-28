arr = [2]
lower = 2
upper = 2
output = [0,1,4,5,7-10,12,14-17,19-74,76-99]
k = 2

ans = []


def add_numbers(l , r):
    for i in range(l+1,r):
        ans.append(str(i))

if arr[0]!=lower:
    arr.insert(0,lower-1)

if arr[-1] != upper:
    arr.append(upper+1)

for i in range(1,len(arr)):
    l = arr[i-1]
    r = arr[i]

    if r-l <= k+1:
        add_numbers(l,r)
    else:
        ans.append(str(l+1)+"-"+str(r-1))

print(ans)
