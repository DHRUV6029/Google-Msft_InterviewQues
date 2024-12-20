#Intervals Merge and Union from 2 lists

#Approach

#Assumption (The list thmeselvves are disjoint and sorted) 

#Intersections


A = [[1,4], [8,10]]
B = [[4,6], [6,8]]


def intersect_list(A , B):
    ans = []
    i = 0
    j = 0

    while i < len(A) and  j < len(B):
        l = max(A[i][0] , B[j][0])
        r = min(A[i][1] , B[j][1])

        if l <= r:
            ans.append((l,r))

        #chech the two pointer
        if A[i][1] < B[j][1]:
            i+=1
        else:
            j+=1
    return ans

# ans = intersect_list(A , B)
# print(ans)



def union_two_list(A, B):
    i = 0 
    j = 0
    cur_interval = None
    ans = []
    while i < len(A) or j < len(B):

        if i>=len(A):
            interval = B[j]
            j+=1
        
        elif j >= len(B):
            interval = A[i]
            i+=1
        else:
            if A[i][0] <= B[j][0]:
                interval = A[i]
                i+=1
            else:
                interval =  B[j]
                j+=1

        #rhis is the fiest interval
        if cur_interval is  None:
            cur_interval = list(interval)
        elif cur_interval[1] >= interval[0]:
            #this is overlap do not start 
            cur_interval[1] = max(cur_interval[1] , interval[1])
        else:
            ans.append(cur_interval)
            cur_interval = interval

    if cur_interval:
        ans.append(cur_interval)

    return ans

def test():
    # Original test case
    test1_A = [[1,5], [10,14], [16,18]]
    test1_B = [[2,6], [8,10], [11,20]]
    print("Test 1:", mergeIntervals(test1_A, test1_B))  # [[1,6], [8,20]]

    # One empty list
    test2_A = [[1,3], [4,6]]
    test2_B = []
    print("Test 2:", mergeIntervals(test2_A, test2_B))  # [[1,3], [4,6]]

    # No overlaps between A and B
    test3_A = [[1,2], [3,4]]
    test3_B = [[5,6], [7,8]]
    print("Test 3:", mergeIntervals(test3_A, test3_B))  # [[1,2], [3,4], [5,6], [7,8]]

    # Complete overlap (B inside A)
    test4_A = [[1,10]]
    test4_B = [[3,5], [6,8]]
    print("Test 4:", mergeIntervals(test4_A, test4_B))  # [[1,10]]

    # Adjacent intervals
    test5_A = [[1,4], [8,10]]
    test5_B = [[4,6], [6,8]]
    print("Test 5:", mergeIntervals(test5_A, test5_B))  # [[1,10]]

    # Single interval lists
    test6_A = [[1,5]]
    test6_B = [[2,3]]
    print("Test 6:", mergeIntervals(test6_A, test6_B))  # [[1,5]]

    # Multiple overlaps
    test7_A = [[1,3], [7,10], [15,20]]
    test7_B = [[2,6], [8,12], [16,18]]
    print("Test 7:", mergeIntervals(test7_A, test7_B))  # [[1,6], [7,12], [15,20]]
    
    # All intervals merge into one
    test8_A = [[1,4], [6,8], [10,12]]
    test8_B = [[3,7], [8,11]]
    print("Test 8:", mergeIntervals(test8_A, test8_B))  # [[1,12]]

test()

        

        

