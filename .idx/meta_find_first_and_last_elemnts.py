
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_lower_bound(target):
            l, r = 0 , len(nums)-1
            ans = -1
            while l <= r:
                mid = (r+l)//2

                if nums[mid] == target:
                    ans = mid
                    r = mid-1

                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return ans
        
        def find_upper_bound(target):
            l, r = 0 , len(nums)-1
            ans = -1
            while l <=r:
                mid = (r+l)//2

                if nums[mid] == target:
                    ans = mid
                    l = mid+1

                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
            return ans


        i = find_lower_bound(target)
        j = find_upper_bound(target)
        
        return [i , j] 
