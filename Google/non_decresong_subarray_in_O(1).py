# Screening Round :


# Given an array of size N, find the maximum length of non-decreasing subarray:
# [0 7 3 10 2 4 6 8 0 9 -20 4]
# ans = 4, [2 4 6 8]


# Follow up:
# You can choose any one index and change its value to any number that you like. What will be the longest non decreasing subarray now:


# In the same example as before, the answer would now be :
# ans = 6, [2 4 6 8 0 9], by changing 0 -> 8 so the subarray becomes non-decreasing.


# Solved using sliding window.


# Verdict : Not recieved feedback yet, but interviewer was very friendly the round went pretty well and I gave approach and code of both the questions in the required time.
# UPDATE : PASSED SCREENING ROUND
# google

nums = [5,4,3,2,1]



def solve(nums):
    ans = 0
    cur = 0
    l = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            ans = max(ans , i-l)
            l = i

    return ans



def solve_followup(nums):
   l = 0
   ans = 0
   changes = 0
   
   for r in range(1, len(nums)):
       if nums[r] < nums[r-1]:
           changes += 1
           
       while l <= r and changes > 1:
           if nums[l] > nums[l+1]:
               changes -= 1
           l += 1
           
       ans = max(ans, r-l+1)
   
   return ans



#print(solve([2 ,4 ,6 ,8, 0 ,9]))
print(solve_followup([9, 2, 1, 1, 1, 1, 1, 9, 1, 1, 1]))
