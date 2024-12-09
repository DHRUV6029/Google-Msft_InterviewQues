class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A ,B = nums1 , nums2

        if len(B) < len(A):
            A, B = B , A

        l ,r = 0 , len(A)-1

        total = (len(A) + len(B))
        half = (len(A) + len(B))//2
        while True:
            i = (r+l)//2
            j = half - i - 2  #2 bcoz we need to account for offset of two

            A_left = A[i] if i >= 0 else float('-inf')
            B_left = B[j] if j >= 0 else float('-inf')

            A_right = A[i+1] if (i+1) < len(A) else  float('inf')
            B_right = B[j+1] if (j+1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                if total % 2:
                    return min(A_right, B_right)
              
                return (max(A_left , B_left) + min(A_right, B_right))/2
                

            if A_left > B_right:
                r = i-1
            else:
                l = i+1
