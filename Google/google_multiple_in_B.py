# given arr A. form arr B from multiples of A of infinte length return kth element(1 based indexing) in arr B after sort B.
# note multiple of 2 are 2,4,6,8,10,12....so on like wise
# constraints:
# 1<A.length<10^5
# 1<k<10^9
# 1<A[i]<10^5
# example testcase:
# given A=[2,3,4]
# b=[2,3,4,4,6,6,8,8,9,......upto infinite]
# kthelement=8(1 based indexing]



#0 is not included as a multople
A = [2, 3, 4]

l=1
r = 10000

k = 8


def find_multiples_smaller_than(mid):
    cnt = 0
    
    for i in range(0 ,len(A)):
        cnt = cnt + (mid/A[i])
        
        if cnt >=k:
            return 1
    
    return 0

ans = 0
while l+1< r:
    mid = (l+r)//2
    
    if find_multiples_smaller_than(mid):
        #means our ans is on the left of mid
        ans = mid
        r = mid
    else:
        l = mid
        
print(r)



