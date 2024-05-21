class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def locate_longest_list(head):
    if not head or not head.next:
        return head

    max_head = head
    max_length = 1

    current_head = head
    current_length = 1

    prev = head
    current = head.next

    while current:
        if current.data <= prev.data:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_head = current_head
            current_length = 1
            current_head = current
        
        prev = current
        current = current.next

    if current_length > max_length:
        max_length = current_length
        max_head = current_head

    # Truncate the list at the end of the found sub-list
    end = max_head
    for _ in range(max_length - 1):
        end = end.next
    end.next = None

    return max_head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

# Test cases
if __name__ == "__main__":
    # Test case 1
    values = [1,2,3,4]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)
    result_head = locate_longest_list(head)
    print("Longest non-increasing sub-list:")
    print_linked_list(result_head)

    # Test case 2
    values = [1, 1, 2, 2]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)
    result_head = locate_longest_list(head)
    print("Longest non-increasing sub-list:")
    print_linked_list(result_head)

    # Test case 3
    values = [3, 2, 1]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)
    result_head = locate_longest_list(head)
    print("Longest non-increasing sub-list:")
    print_linked_list(result_head)

    # Test case 4
    values = [5, 4, 3, 2, 1, 1, 2, 2, 3]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)
    result_head = locate_longest_list(head)
    print("Longest non-increasing sub-list:")
    print_linked_list(result_head)

    # Test case 5
    values = [1]
    head = create_linked_list(values)
    print("Original list:")
    print_linked_list(head)
    result_head = locate_longest_list(head)
    print("Longest non-increasing sub-list:")
    print_linked_list(result_head)
