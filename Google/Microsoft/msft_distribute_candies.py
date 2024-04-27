n = 5
limit = 2
ans = 0

triplets = []


for i in range(n+1):  # Range up to 6 since we're dealing with non-negative integers
    for j in range(n+1):
        for k in range(n+1):
            if i + j + k == n and i<=limit and  j<=limit  and k <= limit:
                ans+=1
                

print(ans)
            
