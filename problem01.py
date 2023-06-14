# Two Pointers Moving at Different Speeds:
# In this scenario, one pointer moves slower than the other. The program finds if there is a loop in a linked list by using two pointers, one moving one step at a time and the other moving two steps at a time. If the pointers meet, it indicates the presence of a loop.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_loop(head):
    slow_ptr = head
    fast_ptr = head

    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            return True

    return False

# Example usage
# Create a linked list with a loop
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3  # Creating a loop

print(has_loop(head))  # Output: True
