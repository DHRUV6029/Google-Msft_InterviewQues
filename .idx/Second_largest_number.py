class Solution:
    def largestNumber(self, nums):
    

        def quick_sort(left, right):
            if left >= right:
                return 
            
            pivot_index = partition(left, right)

            quick_sort(left,pivot_index-1)
            quick_sort(pivot_index+1 , right)

        def compare(x,y):

            return int(str(x)+(str(y))) > int(str(y)+ (str(x)))


        def partition(left,right):
            pivot = nums[right]
            left_front = left

            for i in range(left, right):
                if compare(nums[i], pivot):
                    nums[left_front], nums[i] = nums[i], nums[left_front]
                    left_front+=1

            nums[left_front], nums[right] = nums[right], nums[left_front]
            return left_front

            
            

            
        
        quick_sort(0,len(nums)-1)
        nums[-1] , nums[-2] = nums[-2], nums[-1]
        print(''.join(str(i) for i in nums))


s = Solution().largestNumber(nums = [1,3,2,5,4])
print(s)
        


                

