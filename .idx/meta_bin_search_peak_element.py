class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    
        def bin_search(nums):
            l , r = 0 , len(nums)-1
            while l < r:
                mid = (r+l)//2
            
                if nums[mid]>nums[mid+1]:
                    #this mid element can be peak
                    r = mid
                else:
                    l = mid+1
        
            return l

        return bin_search(nums)
