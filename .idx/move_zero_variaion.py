# 283. Move Zeroes
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

    
class Solution:

    def moveZeroesToBack(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        z_idx = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:

                if nums[z_idx] == 0:
                    nums[z_idx] , nums[i] = nums[i] , nums[z_idx] 
                
                z_idx+=1
        
        return nums
        
    
    def moveZeroesToFront(self, nums) -> None:
        z_idx = len(nums)-1

        for i in range(len(nums)-1 , -1,-1):
            if nums[i]!=0:

                if nums[z_idx]==0:
                    nums[z_idx] , nums[i] = nums[i] , nums[z_idx] 
                
                z_idx-=1

        return nums


s= Solution().moveZeroesToBack([1,2,3,0,0,4,0])
print(s)
s= Solution().moveZeroesToFront([1,2,3,0,0,4,0])
print(s)
