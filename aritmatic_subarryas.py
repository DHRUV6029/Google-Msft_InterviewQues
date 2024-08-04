Round 3: Onsite round 1
It started with a brief introduction and then the interviewer posted the problem.

Given an array of numbers, find all the subarrays which are forming good arithmetic sequence(AP).A good arithmetic sequence is a sequence of numbers having common difference equals to -1 or 1.
E.g {1,2,3} and {3,2,1} are good arithmethic sequence with common difference 1 & -1 respectively.

I came up with a brute force solution. The interviewer asked me to further optimize the solution. I was able to come up with an O(n) soliution and the interviewer was happy with the solution.

Further, I was asked to write the use cases for unit testing the same code.


nums = [1,2,1,0,-1]

dp = [0]*len(nums)


for i in range(2, len(nums)):
    if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        dp[i] = 1 + dp[i-1]

print(sum(dp))
