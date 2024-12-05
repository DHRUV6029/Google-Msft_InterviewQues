class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #if here are duplicates hoareor partitipn does not scale weel 




        def quick_select(nums, k):
            left  , right , mid  = [], [] , []
            pivot = random.choice(nums)

            for i in range(0,len(nums)):
                if nums[i] < pivot:
                    right.append(nums[i])
                elif nums[i] > pivot:
                    left.append(nums[i])
                else:
                    mid.append(nums[i])
            

            if k <= len(left):
                return quick_select(left , k)
            
            if len(left) + len(mid) < k:
                return quick_select(right , k-len(left)-len(mid))
            
            return pivot
        
        return quick_select(nums, k)
