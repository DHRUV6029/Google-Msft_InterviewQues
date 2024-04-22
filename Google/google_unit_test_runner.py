# There is a testRunner funtion that takes multiple unit test and returns if those uts are executed together & then there is some error or not. If no error then return true other wise false. You have been given N unit tests, and you know that when you run all test cases at a time then it fails. Now you need to find at least one pair of UTs, which fails when executed at the same time using the test runner.

# Its easy when we assume that the testRunner takes O(1) to execute any number of test cases. But for the case when the test runner takes O(n) time to execute n test cases at a time then find the optimal way to find one pair of failed UTs.

# Note there may be multiple pairs that fail with each other, but need to report only one. Also all the UTs are running ok when executed individaullay.

# Any suggestion on how to solve this with optimal manner?


#assume unit tests are given as array 



nums = [3,5,2,4,2,54,2,5,2]

failing_pairs = [13,5]
#output ---> (3,4) 

def test_case_runner(n):
    return failing_pairs[0] in n and failing_pairs[1] in n


def cross_batch_comparison(a, b):
    if (failing_pairs[0] in a and failing_pairs[1] in b) or (failing_pairs[1] in a and failing_pairs[0] in b):
        return failing_pairs
         
    
def find_failing_pairs(nums , s , e):
    if e-s==1:
        return [nums[s], nums[e]]
    
    mid = (s + e)//2
    
    l = test_case_runner(nums[s:mid])
    r = test_case_runner(nums[mid:e])
    
    if l and r:
        #result is in both the halves
        return find_failing_pairs(nums, s , mid)   #we need to find only one pair so lets find in left most part
    
    else:
        if l:
            return find_failing_pairs(nums , s, mid)
        elif r:
            return find_failing_pairs(nums , mid ,e)
        else:
            return cross_batch_comparison(nums[s:mid], nums[mid:e])  #WHEN BOTH the halves pass need a cross
        
        
print(find_failing_pairs(nums , 0 , len(nums)-1))
        