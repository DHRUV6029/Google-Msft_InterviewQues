class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = 0
        diff = float('inf')

        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[i-1]:
                pivot = i-1
                break
        
        #find the largest num with min diff
        j = 0
        for i in range(pivot+1,len(nums)):
            if nums[i] > nums[pivot]:
                if nums[i] - nums[pivot] <= diff:
                    diff = nums[i] - nums[pivot]
                    j = i

        if pivot != -1:
            nums[pivot] , nums[j] = nums[j] , nums[pivot]

        #reverse 
        l = pivot+1
        r = len(nums)-1

        while l < r:
            nums[l] , nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        return nums


        
