class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(x ,y):
            return x**2 + y**2

        def choose_pivot(nums , left , right):
            return nums[left+(right-left) // 2]

        def partition(points , left , right):
            pivot = choose_pivot(points , left , right)
            pivot_dist = get_dist(pivot[0] ,pivot[1])

            #all with dsit less than pivot will on left
            while left < right:
                if get_dist(points[left][0] ,points[left][1]) >= pivot_dist:
                    points[left] , points[right] = points[right] ,points[left]
                    right-=1
                else:
                    left+=1

            if get_dist(points[left][0] ,points[right][1]) < pivot_dist:
                left+=1
            return left


        def quick_select():
            left , right = 0 ,len(points)-1
            pivot_idx = len(points)

            while pivot_idx != k:
                pivot_idx = partition(points, left , right)

                if pivot_idx < k:
                    left= pivot_idx
                else:
                    right = pivot_idx-1

            return points[:k]


        return(quick_select())

       
