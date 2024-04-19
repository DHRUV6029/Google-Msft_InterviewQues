# You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

# For example, if you have a ribbon of length 4, you can:
# Keep the ribbon of length 4,
# Cut it into one ribbon of length 3 and one ribbon of length 1,
# Cut it into two ribbons of length 2,
# Cut it into one ribbon of length 2 and two ribbons of length 1, or
# Cut it into four ribbons of length 1.
# Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

# Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.

ribbons =[5,7,9]
k = 22


if sum(ribbons) < k:
    print(0)
    
ans = 0


def can_cut(mid):
    cnt = 0
    
    for i in range(0,len(ribbons)):
        cnt+=(ribbons[i]//mid)
        
    return cnt > k

l = 1
r =max(ribbons)

while l < r:
    mid = (l+r)//2
    
    if can_cut(mid):
        l = mid+1
        ans = mid
    else:
        r = mid
        
print(r)