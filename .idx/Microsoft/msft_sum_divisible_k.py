import collections
digits =[0,0,0,0,0,1]

freq = [0]*10
s = 0


m1 = [1, 4, 7, 2, 5, 8]
m2 = [2,5,8,1,4,7]
def create_number(arr):
    
    ans= ''
    for i in range(0 , len(arr)):
        if arr[i]>0:
            ans+=(str(i)*arr[i])
            
    ans = ans[::-1]  #take care of the leading zeros
    i = 0
    while i <len(ans) and ans[i] == '0':
        i+=1
    ans  = ans[i:]
    if ans == '' and freq[0]>0:
        return '0'
    else:
        return ans


for i in range(0,len(digits)):
    freq[digits[i]]+=1
    s+=digits[i]
    

    
while s and s  % 3 !=0:
    select = None
    if s % 3 == 1:
        select = m1

    elif s%3 == 2:
        select = m2
        
    for i in select:
        if freq[i]>0:
            freq[i]-=1
            s-=i
            break

        
ans = create_number(freq)
print(ans)
    
