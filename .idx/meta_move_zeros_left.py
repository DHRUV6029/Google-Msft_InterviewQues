class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #fnid the furst existance if 
        zero_idx =  len(nums)

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                zero_idx = i
                break


        #all the values before this will already be in-place 

        i = zero_idx
        while i >= 0:
            if nums[i]!=0:
                nums[zero_idx] , nums[i] = nums[i] , nums[zero_idx]
                zero_idx-=1
            i-=1


        print(nums)

s = Solution().moveZeroes(nums =  [0,1,0,3,12])
