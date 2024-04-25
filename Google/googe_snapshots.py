# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 
import collections
import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.records = collections.defaultdict(list)
        self.id = 0
        
    def set(self, index: int, val: int) -> None:
        self.records[self.id].append([val , self.id])
        
    def snap(self) -> int:
        self.id+=1
        return self.id-1
        

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect_right(self.records[index] , [10**9 , snap_id])-1
        return self.records[index][idx][0]
        


# Your SnapshotArray object will be instantiated and called as such:
snapshotArr = SnapshotArray(3)
snapshotArr.set(0,5); 
snapshotArr.set(0,6); 
snapshotArr.set(0,9); 
snapshotArr.snap(); 

print(snapshotArr.get(0,0));  