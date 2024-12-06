class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #approach as the solution asks for in-mem or inplace merge 

        p1 = m-1
        p2 = n-1

        i = m+n-1

        for i in range(m+n-1, -1, -1):
            if p2 < 0:
                break
            #compare the p1 and p2 elements 
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1-=1
            else:
                nums1[i] = nums2[p2]
                p2-=1

        print(nums1)

s= Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
