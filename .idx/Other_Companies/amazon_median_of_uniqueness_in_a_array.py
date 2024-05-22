class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def count_subarray_with_less_than_k(mid):
            l = 0
            mp = collections.defaultdict(int)
            cnt = 0
            for r in range(len(nums)):
                mp[nums[r]]+=1
         
                while len(mp) > mid:
                    mp[nums[l]]-=1
            
                    if not mp[nums[l]]:
                        mp.pop(nums[l])
                
                    l+=1
            
                cnt+=r-l+1
        
            return cnt


        n = len(nums)
        l =   0   
        r = n-1

        total = ((n) * (n+1))//2

        md = (total - 1 )//2

        while l <=r:
            mid = (l+r)//2
    
            if count_subarray_with_less_than_k(mid) > md :
                r = mid-1
            else:
                l = mid+1
        
        return(l)
            
        
        
        


        
