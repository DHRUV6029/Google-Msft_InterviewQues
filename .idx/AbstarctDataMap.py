class Node:
    def __init__(self, val = None ,key =None ,next = None , prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class AbstractDataMap:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.mp = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def __add_node(self , node):
        tmp = self.tail.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.tail
        self.tail.prev = node

    def __remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev



    def get(self, key):
        if key not in self.mp:
            return -1 #or throw error 
        
        node = self.mp[key]
        self.__remove_node(node)
        self.__add_node(node)
        

    
    def remove(self, key):
        self.__remove_node(self.mp[key])

    def put(self, key , val):
        if key in self.mp:
            self.__remove_node(self.mp[key])

        node = Node(val,key)
        self.__add_node(node)
        self.mp[key] =node

    def last_used(self):
        return self.tail.prev.key



obj = AbstractDataMap()
obj.put("a" , 1)
obj.put("b" , 2)
obj.put("b" , 2)
print(obj.last_used())
