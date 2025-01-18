class ListNode:
    def __init__(self, val = None , next = None):
        self.val = val
        self.next = next



class App:
    def __init__(self):
        pass

    def Solution(self, l1 , l2):
        i , j = 0 ,0

        while l1 and l2:

            if i >= len(l1.val): #rest
                i = 0
                l1 = l1.next
            
            if j >= len(l2.val): #rest
                j = 0
                l2 = l2.next

            while l1 and not l1.val: #skip
                l1 = l1.next

            while l2 and not l2.val: #skip
                l2 = l2.next
            
            
            
            if not l1 or not l2: #end
                break
            
            #compare
            if l1.val[i] == l2.val[j]:
                i+=1
                j+=1
            else:
                return False
            
        return True if not l1 and not l2 else False
            

l = ListNode("hello")
l.next = ListNode("l")


l1 = ListNode("h")
l1.next = ListNode("e")
l1.next.next = ListNode("l")
l1.next.next.next = ListNode("l")
l1.next.next.next.next = ListNode("o")


s = App().Solution(l,l1)
print(s)

