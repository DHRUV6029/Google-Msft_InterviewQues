#consecutive sequence sum 
def solution(arr, target):
    arr.sort()

    l = 0
    r = 0
    cur_sum = 0
    while r < len(arr):
        if r == 0 or (r > 0 and arr[r] - arr[r-1]==1):
            cur_sum+=arr[r]
        else:
            l = r #shift l tp r 
            cur_sum = arr[r]


        while l <= r and cur_sum > target:
            cur_sum-=arr[l]
            l+=1

        if cur_sum == target:
            return True
        r+=1
    return False

s = solution(arr = [1,3,5,7,8,8], target = 16)
print(s)
