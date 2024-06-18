Problem 2: Frog Game
Given an array blocks where each cell represents the height of the current block, two frogs start on the same block. Each frog can only jump to another adjacent block if it is higher or equal to the one it is on. Return the maximum distance that can be between the two frogs if they can start together on any block.

Examples:

For input [9,2,5,3,0], the answer is 2. Let the two frogs start on cell 4 and one of them go to cell 2. (There is another option here that will give you 2).
For input [1,2,3,4,5,8], the answer is 6. If both frogs start at cell 5.


nums =  [9,2,5,3,0]

left = [1]*len(nums)
right = [1]*len(nums)


for i in range(1 ,len(nums)):
    if nums[i] <= nums[i-1]:
        left[i] = left[i-1]+1

        
for j in range(len(nums)-2, -1, -1):
    if nums[j] <= nums[j+1]:
        right[j] = right[j+1]+1

        
ans = 0

for k in range(0 , len(left)):
    ans = max(ans, (left[k]+right[k]))
    
print(ans-1)
