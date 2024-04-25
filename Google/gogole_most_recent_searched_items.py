# Hello all, Just wanted to share my recent experience for google phone screen round

# Time: 45 minutes
# Question: i dont remember exact wording but the structure is as follows:

# Q) Design a system/data structure to given the user Top N Most Recently Searched Items



class DoubleLinkedList:
    def __init__(self, val , prev, next) -> None:
        self.prev = None
        self.next = None
        self.val = val  #search terms
        
class MostRecentlySearched:
    def __init__(self) -> None:
        self.head = DoubleLinkedList("", None , None) #sentinel head what follows are MRUs
        self.tail = DoubleLinkedList("", None , None)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def topNRecentlySearched(self,N):
        #twp cases if a user just clicks on the search bar : how google
        #search works displays top K 
        cur = self.head
        res = []
        while N and cur.next is not None:
            res.append(cur.next.val)
            cur = cur.next
            N-=1
            
        return res
    
    def addSearchedWord(self, word):
        node = DoubleLinkedList(word , None , None)
        next_of_this = self.head.next
        
        #first set this node next and prev pointets
        node.next =next_of_this
        next_of_this.prev = node
        
        #set the head next and prev ppointets
        self.head.next =node
        node.prev =self.head
        
        print("frfr")
        
        

m = MostRecentlySearched()
m.addSearchedWord("john")
m.addSearchedWord("inni")
m.addSearchedWord("johnny")
m.addSearchedWord("hanah")
m.addSearchedWord("brinda")

print(m.topNRecentlySearched(3))
            
        
        
        