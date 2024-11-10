arr = [4 , 9 , 0 , 2]
k = 2

#need to remoce n-k smallest elemnts will be left with k largest

st = []
k = len(arr)-k
for i in range(0,len(arr)):
    while st and k and arr[st[-1]] < arr[i]:
        st.pop()
        k-=1
    st.append(i)

st = st[:k] if k else st

ans = 0

for i in st:
    ans = ans *10 + arr[i]

print(ans)
