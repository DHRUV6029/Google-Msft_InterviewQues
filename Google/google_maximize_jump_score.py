# Hi all,

# I came across a coding question in my recent interview which is mentioned below :

# Given an array of non-negative integers, the goal is to travel from the first index to the last index with maximum possible score with as many jumps allowed. Score of a jump is defined as the number of index jumped multiplied by the value on the jumped index.
# e.g. [3,7,9,10]

# if the jump is from index0 to index2, the score is (2-0)*9 = 18

# Sample input: [3,12,9,10]
# Sample output: 32
# Explanation: jump from index0 to index1 and then to index3 = (1-0) * 12 + (3-1) * 10 = 12 + 20 = 32

# What are the possible ways to approach this problem? Can it be done in better than O(n^2) ?


#Approach -< how to maximize the jump score
#for any point i we can jump to a more larger number than i score (j-i)*nums[j]

#IS it tru

arr =  [3,12,9,10]
st = []  #seedn value
ans = 0
st = []
for i in range(0,len(arr)):
    while st and arr[st[-1]] <= arr[i]:
        st.pop()
        
    st.append(i)
    
    
ans = 0

while st:
    idx = st.pop()
    
    ans =  ans + arr[idx]*(idx - (st[-1] if st else 0))
    
print(ans)