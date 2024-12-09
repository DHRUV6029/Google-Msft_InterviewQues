class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
       
        if not nums:
            return [[lower,upper]]

        ans = []
       

        if nums[0] > lower:
            ans.append((lower  , nums[0]-1))

        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]-1:
                l = nums[i-1]+1
                r = nums[i]-1

                ans.append((l, r))

        if nums[-1] != upper:
            ans.append((nums[-1]+1 , upper))

        return ans
