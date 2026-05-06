# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Insert at beginning
def insert_beginning(head, data):
    new_node = Node(data)

    if head is not None:
        head.prev = new_node
        new_node.next = head

    return new_node

# Print DLL
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

# Example usage
head = None

head = insert_beginning(head, 30)
head = insert_beginning(head, 20)
head = insert_beginning(head, 10)

print("Doubly Linked List:")
print_list(head)