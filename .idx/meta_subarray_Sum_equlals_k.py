class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)

        mp[0] =  0
        cur = 0
        ans = 0
        for i in range(0,len(nums)):
            cur+=nums[i]

            if cur == k: ans+=1

            if cur - k in mp:
                ans+=(mp[cur-k])

            mp[cur]+=1

        return ans


      
