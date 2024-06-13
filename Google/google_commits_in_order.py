# Given a list of offsets, ordered by when they are processed, return a list of offsets that represent the greediest order of commits.
# That is, when an offset CAN be committed, we MUST commit it.

# We can commit an offset X when EITHER:

# X = 0, since it is the first message of the stream
# All offsets < X are either ready to be committed or are already committed
# If we cannot commit offset X, we represent this as -1.

# Example 1:
# Input: [2, 0, 1]
# Output: [-1, 0, 2]

# Example 2:
# Input: [0, 1, 2]
# Output: [0, 1, 2]

# Example 3:
# Input: [2, 1, 0, 5, 4]
# Output: [-1, -1, 2, -1, -1]

# We never have duplicate offsets.

# Follow-up do it in O(n) time and O(1) space complexity

# google
# phone

nums=[]

arr = [2,0,1,4,3,6]

need = 0
have = 0
offset = 0
for i in range(0 ,len(arr)):
    have = arr[i]

    if need == have:
        nums.append(i)
        
        need+=1
    else:
        nums.append(-1)


print(nums)
