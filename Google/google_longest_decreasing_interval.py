# question :
# The problem is to find the longest interval over which the value has decreased, but the interval doesn't have to be consecutive
# {50,52,58,54,57,51,55,60,62,65,68,72,62,61,59,63,72}
# Ans : 7 (index 14 - index 7)

# Solution i gave


nums =[6,0,8,2,1,5]


nums = nums[::-1]
#Arroach
st = []
max_val = 0
for i in range(0 ,len(nums)):
    while st and nums[st[-1]] > nums[i]:
        max_val =  max(max_val , i-st[-1])
        st.pop()
        
    st.append(i)
    
print(max_val)