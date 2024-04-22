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