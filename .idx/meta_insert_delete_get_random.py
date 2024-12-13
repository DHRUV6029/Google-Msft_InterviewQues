class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.mp = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.mp[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False

        

    def remove(self, val: int) -> bool:
        #Logic to remove the number How to do it in O(1)
        #Move the val to last index and value at last index to the value it was present 
        if val in self.mp:
            org = self.mp[val]
            last_element = self.arr[-1]
            self.arr[org] , self.arr[-1] = last_element , val 

            #array exchange done
            self.mp[last_element] = org
            self.arr.pop()
            self.mp.pop(val)  
            return True      
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
