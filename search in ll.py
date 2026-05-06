# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Search in linked list
def search(head, key):
    temp = head

    while temp:
        if temp.data == key:
            return True
        temp = temp.next

    return False

# Example usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

key = 30

if search(head, key):
    print("Element Found")
else:
    print("Element Not Found")