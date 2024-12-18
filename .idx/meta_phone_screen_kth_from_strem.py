# Real Phone Screen

# You are given an API readNext() which gives you the next (positive) 
# number in a stream. The end of the stream is indicated by a -1. 
# Return the Kth smallest element in this stream.
# Example: [2, 3, 5, 4, 6, 7, 9, 11, 2, 3 ... -1], k = 3. The method should return 4.

#Here the method retuens 4 (duplicates need to be handled)

k =3
class ArrayIterator:
    def __init__(self):
        self.arr = [2, 3,-1]
        self.idx = 0

    def readNext(self ):
        val = self.arr[self.idx]
        self.idx+=1

        return val
    

iter = ArrayIterator()
max_heap = []
seen = set()

while True:
    val = iter.readNext()
    if val == -1:
        ans = -max_heap[0] if len(max_heap)==k else None
        print(ans)
        break

    if val not in seen:
        heapq.heappush(max_heap , -val)

        seen.add(val)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

