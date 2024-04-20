
#what is the crux

#find  two indexes such that nums[i] <-= nums[j] also maximixing (j-i)

#so for 6 we need larger elemnt than 6 but need to maximize the distance

#So the problem boils down to the following at every index i find a index rightmost j such
#that nums[i] <-= nums[j]

# #Approch 

# from back we can keep a track of elements in a decreasing order

# [0,1,5]-> we will keep the indexed

# [2,5]  <- keep increasing from back

# traverse from right -> 6
nums = [9,8,1,0,1,9,4,0,4,1]
st = []

for i in range(len(nums)-1, -1 ,-1):
    if not st or nums[st[-1]] <= nums[i]:
        st.append(i)
        
for i in range(0,len(nums)):
    while st and nums[st[-1]] >= nums[i]:
        ans =  st[-1] - i
        st.pop()
        
print(ans)

print((2+3)*4)