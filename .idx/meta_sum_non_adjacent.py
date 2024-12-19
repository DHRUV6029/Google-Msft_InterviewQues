
arr = [1,1,1,90]

ans = 0

a = arr[0]
b = 0 

for i in range(1 ,len(arr)):
    ans = max(a , b+arr[i])

    #here if we are taking this num then 
    #next turn b becmomes a and a becmome b
    tmp =a
    a = b+arr[i]
    b = tmp


print(ans)
    
