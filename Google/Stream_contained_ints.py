import collections



s = "11222233 3333 4556 6777 8888"
k =4

class ContainedElements:
    
    def __init__(self) -> None:
        self.ele_to_container = collections.defaultdict(int)
        self.stale = set()
        self.container = collections.defaultdict(set)
        self.ele_num = -1
        self.prev = 0 
       
        
        
    def addElement(self, val):
        self.ele_num+=1
        container_id = self.ele_num // k
        
        #decide to put in this cintainer also need to check in prec
       
        #check if we have this element already in current container
        #or any other containewr
        
        if val in self.ele_to_container:
            #if yes then is it in anyother container 
            if container_id != self.ele_to_container[val]:
                
                #need to put all those in stale
                prev_cont = self.ele_to_container[val]
                if val in self.container[prev_cont]:
                    self.container[prev_cont].remove(val)
                    self.stale.add(val)
                    self.prev = val
                    
        else:
            
            self.ele_to_container[val]=container_id
            
        if val not in self.stale:
            self.container[container_id].add(val)
            
    def build_state(self):
        return self.container
        
            

            
            
                    


s = ContainedElements()

s.addElement(1)
s.addElement(1)
s.addElement(2)
s.addElement(2)

s.addElement(2)
s.addElement(2)
s.addElement(3)
s.addElement(3)

s.addElement(3)
s.addElement(2)
s.addElement(3)
s.addElement(3)

s.addElement(6)
s.addElement(7)
s.addElement(7)
s.addElement(7)

s.addElement(4)
s.addElement(5)
s.addElement(5)
s.addElement(6)


s.addElement(8)
s.addElement(8)
s.addElement(8)
s.addElement(8)


print("rfrf")







                    
                    
        
        
    
