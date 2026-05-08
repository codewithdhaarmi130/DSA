# Reverse a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Reverse function
def reverse_ll(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev

# Print linked list
def print_list(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")

# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original Linked List:")
print_list(head)

# Reverse linked list
head = reverse_ll(head)

print("Reversed Linked List:")
print_list(head)