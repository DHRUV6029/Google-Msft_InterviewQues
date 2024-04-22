# Given an array of integers, find a subarray with maximum sum?

# Solved using Kadane's Algorithm

# Follow up:
# Given an array of integers nums, find indexes [i, j] such that the subarray sum nums[i] + nums[i+1] ... nums[j-1] + nums[j] is maximum and nums[i] is equal to nums[j]

# Example:

# nums = [1, 3, 5, 6, 3, -6, 23]

# Answer: [1, 4]


nums = [1, 3, 5, 6, 3, -6, 3]

prefix_map = {}
prefix_arr = []
cur = 0
for i in range(0,len(nums)):
    cur+=nums[i]
    prefix_arr.append(cur)
    prefix_map[cur] = i


prefix_map[0] = -1
    
cur_sum = nums[0]
max_sum = nums[0]
s , e = 0, 0

for i in range(1 ,len(nums)):
    cur_sum = max(cur_sum + nums[i] , nums[i])
    if max_sum<= cur_sum:
        e = i
        s = prefix_map[prefix_arr[i] - cur_sum]+1
        max_sum = cur_sum
    
    
print(s, e)
