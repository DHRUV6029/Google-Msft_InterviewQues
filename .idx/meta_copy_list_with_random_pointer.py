"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        #step -1 create a next pointer weaved linked list
        ptr = head
        
        while ptr is not None:
            new_node = Node(ptr.val , None , None) #create a cloned node

            #link the nodes
            new_node.next = ptr.next
            ptr.next = new_node


            ptr = new_node.next

        #now link the random nodes
        ptr = head

        while ptr is not None:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next


        #unweave the New Cloned linked list
        ptr_old = head
        ptr_new = head.next

        newHead = head.next

        while ptr_old is not None:
            ptr_old.next = ptr_old.next.next
            ptr_new.next =  ptr_new.next.next  if ptr_new.next else None

            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return newHead
        
