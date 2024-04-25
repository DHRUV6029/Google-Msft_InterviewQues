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
# A = [3, 7]
# #[3,6,7,9,12,14,15,18,21]
# l=1
# r = 10**9

# k = 9


# def find_multiples_smaller_than(mid):
#     cnt = 0
    
#     for i in range(0 ,len(A)):
#         cnt = cnt + (mid/A[i])
        
#         if cnt >=k:
#             return 1
    
#     return 0

# ans = 0
# while l+1< r:
#     mid = (l+r)//2
    
#     if find_multiples_smaller_than(mid):
#         #means our ans is on the left of mid
#         ans = mid
#         r = mid
#     else:
#         l = mid
        
# print(r)

# def count_elements(arr, x):
#     """
#     Counts the number of elements that are less than or equal to x
#     """
#     count_smaller, count_equal = 0, 0
#     for num in arr:
#         count_smaller += x // num
#         if x % num == 0:
#             count_equal += 1
#             count_smaller -= 1
#     return count_smaller, count_equal

# def find_kth_element(arr, k):
#     left, right = 1, 2
#     # Expand the search space until it definitely contains the kth element
#     while count_elements(arr, right)[0] < k:
#         left = right
#         right *= 2
#     print(left, right)
#     # Binary search within the defined range
#     while left < right:
#         mid = (left + right) // 2
#         count_smaller, count_equal = count_elements(arr, mid)

#         if count_smaller < k and count_smaller + count_equal >= k:
#             return mid
#         elif count_smaller >= k:
#             right = mid
#         else:
#             left = mid + 1

#     return left

# print(find_kth_element([2,3,4], 5))



def find_kth_multiples_of(nums, k):
    left, right = 0,100
    ans = float("inf")
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for x in nums:
            count += mid // x
        if count >= k:
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1
    return ans

print(find_kth_multiples_of([3,7], 9))