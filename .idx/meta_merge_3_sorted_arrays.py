class Solution:
    def mergeThreeSortedArrays(self, nums1 , nums2 , nums3):
        #approach as the solution asks for in-mem or inplace merge 

        ans = []

        i, j , k = 0,0, 0

        while i < len(nums1) or j < len(nums2) or k <len(nums3):

            v1 = float('inf') if i >= len(nums1) else nums1[i]
            v2 = float('inf') if j >= len(nums2) else nums2[j]
            v3 = float('inf') if k >= len(nums3) else nums3[k]

            if v1 <= v2 and v1 <= v3:
                ans.append(v1)
                i+=1
            elif v2 <= v1 and v2 <= v3:
                ans.append(v2)
                j+=1
            elif v3 <= v1 and v3 <= v2:
                ans.append(v3)
                k+=1

        return ans


s= Solution().mergeThreeSortedArrays([2,3,5,6] , [4,5,6] , [1])
print(s)
