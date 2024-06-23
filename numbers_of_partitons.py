
# Find the number of partitions of an array such that each contiguous partition consists of atleast one negative number.
# eg. [-1,-2,-3,-4] has these possible partitions :
# [-1],[-2],[-3],[-4];
# [-1,-2],[-3,-4];
# [-1,-2,-3] ,[-4];
# [-1],[-2,-3,-4];
# [-1][-2,-3],[-4];
nums = [1,2,3,4]

memo = {}

def solve(idx , is_neg):
    if idx == len(nums):
        return 1 if is_neg else 0
    
    if (idx , is_neg) in memo:
        return memo[(idx , is_neg)]
    
    res = 0
    #pick or no pick 
    res+=solve(idx+1 , is_neg or (nums[idx]<0)) #value remain the same as no partiron is there

    #partitoan here if and only if we ahve a negatice values
    if is_neg:
        res+=solve(idx+1 , True if nums[idx] < 0 else False)
    
    memo[(idx , is_neg)] = res
    return res

print(solve(0 , False))

