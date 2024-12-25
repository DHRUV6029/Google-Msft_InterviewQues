nums = [1,100]
x = 5

l = 0
r = len(nums)-1
closet  = float('inf')
ans = [0,0]
while l < r:
    if nums[l] + nums[r] == x:
        print (nums[l] , nums[r])
        break
    else:
        
        if closet >= abs(x - (nums[l]+nums[r])):
            closet = abs(x - (nums[l]+nums[r]))
            ans[0] , ans[1] = [nums[l], nums[r]]


        if nums[l]+nums[r] > x:
            r-=1
        else:
            l+=1

print(ans)
