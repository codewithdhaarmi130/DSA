# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Find length
def get_length(head):
    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next

    return count

# Example usage
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Length of linked list:", get_length(head))