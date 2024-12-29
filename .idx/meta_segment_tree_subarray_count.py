#Count num of 1s oin subarray immuatble 

# class Solution:
#     def __init__(self , arr) -> None:
#         self.prefix  =[]


#         self.prefix  =[1 if arr[0] == 1 else 0]

#         for i in range(0,len(arr)):
#             self.prefix.append(self.prefix[i-1]+arr[i])

#     def query(self, l ,r):
#         if l ==0:
#             return self.prefix[r]
#         else:
#             return self.prefix[r] - self.prefix[l-1]
        

# s = Solution([1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1])
# print(s.query(1, 3))
# print(s.query(3, 5))







class SegmentTree:
    def __init__(self , arr) -> None:
        self.tree = [0]*(4*len(arr)+1)
        self.LEFT , self.RIGHT = 0 , len(arr)-1
        

        self.__buildtree(arr, 0 , self.LEFT , self.RIGHT)

    def __buildtree(self, nums , index , s_left , s_right):
        if s_left == s_right:
            self.tree[index] =nums[s_left]
            return
        mid = s_left + (s_right - s_left)//2

        self.__buildtree(nums , 2*index+1 , s_left , mid)
        self.__buildtree(nums, 2*index+2 , mid+1 , s_right)

        self.tree[index] = self.tree[2*index+1] + self.tree[ 2*index+2]

    def query(self, l , r):
        return self.__query(0 ,  l , r , self.LEFT , self.RIGHT)
    
    def update(self, index, val):
        return self.__update(0, index , val , self.LEFT, self.RIGHT)
    
    def __query(self , index, q_left , q_right , s_left , s_right):
        #cjheck out of baunfday conditons
        if s_left > q_right or s_right < q_left:
            return 0 
        
        if q_left <= s_left and s_right <= q_right:
            return self.tree[index]
        
        mid = s_left + (s_right - s_left)//2
        left = self.__query( 2*index+1 ,q_left , q_right, s_left , mid)
        right = self.__query( 2*index+2 ,q_left , q_right, mid+1 , s_right)
        
        return left+right
    
    def __update(self, index, node, val , s_left, s_right):
        if s_left == s_right:
            self.tree[index] = val
            return
        else:
            mid = s_left + (s_right - s_left)//2
            if node <= mid and node >= s_left:
                self.__update(2*index+1 , node, val , s_left, mid)
            else:
                self.__update(2*index+2 , node, val , mid+1, s_right)

            self.tree[index]  = self.tree[2*index+1] + self.tree[ 2*index+2]


s = SegmentTree([1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1])

ams = s.query(0,4)
print(ams)


            
        
