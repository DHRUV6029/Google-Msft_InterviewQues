class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for i in range(0,len(nums)):
                count[nums[i]]+=1

        nums = list(count.keys())

        def choose_pivot(left, right,nums):
            return nums[left + (right - left)//2]
        
        def get_comparison_metric(x):
            return count[x]


        def partition(left, right , nums):
            pivot = choose_pivot(left, right,nums)
            pivot_freq = get_comparison_metric(pivot)

            while left < right:
                if get_comparison_metric(nums[left]) <= pivot_freq:
                    nums[left] , nums[right] = nums[right] , nums[left]
                    right-=1
                else:
                    left+=1
            

            #we need pivot "left after the k th elements for ef [4,3,2,1]"
            
            if get_comparison_metric(nums[left]) > pivot_freq:
                left+=1
            
            return left
        
        def quick_select(nums, k):
            #here largest will be on the left side and smallest on the left sid

            left , right = 0 , len(nums)-1
            pivot_idx = len(nums)   #currenlty taking the last index as the pivot index

            while pivot_idx != k:
                #[5,4,2,1]   pivot_idx = 3 means [5,4] is the answer
                pivot_idx = partition(left, right , nums)

                
                #case-1 
                if pivot_idx < k:
                    #need to move right
                    left = pivot_idx
                else:
                    right = pivot_idx - 1

            return nums[:k]
        
    
        return quick_select(nums, k)
        
        
