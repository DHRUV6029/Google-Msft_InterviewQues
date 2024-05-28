#this is the 
class SegmentTree:
    def __init__(self , arr) -> None:
        self.arr =arr
        self.seg_tree = [0]*(4*len(self.arr)+1)


    def build(self, idx , start, end):
        if start == end:
            self.seg_tree[idx] = self.arr[start]
            
        else:
            mid = (start + end)//2

            #recurse on the left
            self.build(2*idx , start , mid)

            #recurcse on the right
            self.build(2*idx+1  , mid+1 , end)

            self.seg_tree[idx] = self.seg_tree[2*idx] + self.seg_tree[2*idx+1]

    def update(self , idx , start , end , i , val):
        if start == end:
            self.seg_tree[idx]+=val
            self.arr[i]+=val     #in range sum value will be the differene


        else:
            mid = (start + end)//2

            if start <= idx and idx <= mid:
                self.update(2*idx , start , mid , i , val)
            else:
                self.update(2*idx+1 , mid+1 , end , i , val)

            self.seg_tree[idx] = self.seg_tree[2*idx] + self.seg_tree[2*idx+1]


    def query(self , idx  , start , end , l,  r):
        #outside the the range
        if (r < start or l > end):
            return 0
        
        #inside the current range
        if (l <= start  and end <= r):
            return self.seg_tree[idx]
        
        mid= (start + end)//2
        left = self.query(2*idx , start , mid , l , r)
        right = self.query(2*idx+1 , mid+1 , end , l , r )

        return (left + right)
    


##########Complelte the boiler plate code#############
#Seg Tree always start from 1
nums= [1,2,3,4,5,6]
s = SegmentTree([1,2,3,4,5,6])
s.build(1 , 0 ,len(nums)-1)

print(s.query(1 , 0 ,len(nums)-1 , 0 , 2))


