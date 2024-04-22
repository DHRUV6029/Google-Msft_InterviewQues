# Given a string, your task is to generate a list of substrings such that while appending all of the substrings in the list should give back the original string. If the resulting substring is not already present in the list, it should be added to the list.

# Examples:

# Input: "GOOOOOOGLE"
# Output: ["G", "O", "OO", "OOO", "GL", "E"]

# Input: "GOOOOOOGLEG"
# Output: ["G", "O", "OO", "OOO", "GL", "E", "G"]
# handling edge case

input=  "GOOOOOOGLEG"

hset =set()
i = 0
l =0
r = 0
ans = []

while r <len(input):
    while r <len(input) and input[l:r+1] in hset:
        r+=1
        
    if input[l:r+1]  not in hset:
        hset.add(input[l:r+1])
        ans.append(input[l:r+1])
        l+=(r-l+1)
        r+=1
   
if input[l:r+1]:    
    ans.append(input[l:r+1])
print(ans)
    
    