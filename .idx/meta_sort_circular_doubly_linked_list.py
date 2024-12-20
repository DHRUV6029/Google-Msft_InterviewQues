class ListNode:
   def __init__(self, val=0, next=None, prev=None):
       self.val = val
       self.next = next
       self.prev = prev



def merge_sort(head):
    
    tail = head.prev
    tail.next = None
    head.prev = None

    #List are unlinked now do a merge sort as you would do in a linked list
    #addition code is two connect two pointers
    new_head = sortCircularDoublyLinkedList(head)
    _, tail  = find_middle_of_cdll(new_head, False)  #finds the tail t0 link circularly
    

    if tail:
        new_head.prev = tail
        tail.next = new_head
    else:
        new_head.next = new_head
        new_head.prev = new_head

    return new_head
    #lINK THEM BACK



def sortCircularDoublyLinkedList(head):
    if not head or not head.next:
        return  head
    
    mid , _ = find_middle_of_cdll(head, True)

    left = sortCircularDoublyLinkedList(head)
    right = sortCircularDoublyLinkedList(mid)

    return merge_two_cdll(left , right)

def merge_two_cdll(list1 , list2):
    dummyHead = ListNode(0)
    tail = dummyHead

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1.prev = tail
            list1 = list1.next
        else:
            tail.next = list2
            list2.prev = tail
            list2 = list2.next

        tail = tail.next
    
    if list1:
        tail.next = list1
        list1.prev = tail
    
    if list2:
        tail.next = list2
        list2.prev = tail
    
    return dummyHead.next

def find_middle_of_cdll(head, flag):
    last = None
    slow ,fast = head , head

    while fast and fast.next:
        last = fast.next
        slow = slow.next
        fast = fast.next.next

    if flag:
        slow.prev.next = None
        slow.prev = None
        
    return slow , last






n1 = ListNode(4)
n2 = ListNode(2)

# Connect forward
n1.next = n2
n2.next = n1  # Make circular

# Connect backward
n2.prev = n1
n1.prev = n2  # Make circular

ans = merge_sort(n1)
print(ans)
