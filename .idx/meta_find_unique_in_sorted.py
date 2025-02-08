arr = [2,2,2,2]


def find_unique_in_sorted(arr):
    i = 0
    cnt = 0
    while i < len(arr):
        target = arr[i]

        l = i
        r = len(arr)-1

        while l <= r:
            mid = (r+l)//2

            if arr[mid] <= target:
                l = mid+1
            else:
                r = mid-1

        i = r+1
        cnt+=1

    return cnt

s = find_unique_in_sorted(arr)
print(s)
