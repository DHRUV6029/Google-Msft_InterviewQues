class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        #process the left here 
        ans[0] = 1
        
        for i in range(1 ,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]

        R=1 
        #approcah why it will worj
        #now the state is at i we have producr of ledt i-1 , now from random
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i]*R
            R = R*nums[i]

        return ans
