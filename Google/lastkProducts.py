# Round - 2 : DSA
# //First Question
# Design a data structure that supports the following three operations.

# a constructor that takes a parameter K
# add(x) -- inserts the number x
# get() -- returns the product of the last K elements inserted
# ex:
# K = 2
# add(2)
# add(3)
# get() -> 6
# add(4)
# get() -> 12

# Clarifications:
# Q: What to return if less than K elements have been inseted? A: Return the product of all inserted elements.
# Q: Can the result overflow / should we use a long? A: The result of get() will always fit in an integer.
# Q: Values of K? A: K is a positive integer.
# Q: Values of x? A: x can be any integer.

# import collections
# class LastKProducts:
#     def __init__(self , k) -> None:
#         self.k = k
#         self.que = collections.deque()
#         self.cur_prod = 1

#     def add(self, x):
#         if len(self.que) == self.k:
#             self.cur_prod/=self.que.popleft()
            
#         self.que.append(x)
#         self.cur_prod*=x

#     def get(self):
#         return self.cur_prod
    
# obj = LastKProducts(2)
# obj.add(1)
# obj.add(2)
# obj.add(5)
# obj.add(1)
# print(obj.get())

# //Follow-up
# What if K is given in the get() function instead of in the constructor?
# My answer-
# •storing all numbers in the array instead of removing from queue
# •could compute the product of last K elements in get(K), but this increase the time complexity O(K)
# •how could we improve time complexity, reusing the same ideas?

# store prefix products in an array -> O(1) time complexity
# do not make the product zero, record the last found 0


class LastKProductsFollow:
    def __init__(self) -> None:
        self.arr = []
        

    def add(self, x):
        if not self.arr:
            self.arr.append(x)
        else:
            self.arr.append(self.arr[-1] * x)

    def get(self , k):
        r = len(self.arr)
        if r <= k:
            return self.arr[-1]
        
        i = r-k-1
        ans = self.arr[-1] / self.arr[i]
        return ans
    
obj = LastKProductsFollow()
obj.add(5)
obj.add(2)
obj.add(5)
obj.add(1)
print(obj.get(3))

    

        
        
