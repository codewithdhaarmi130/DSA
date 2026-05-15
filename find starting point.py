class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findStartingPoint(head):
    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # No loop
    if fast is None or fast.next is None:
        return None

    # Move slow to head
    slow = head

    # Move both one step
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# Create linked list
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create loop
fifth.next = third

start = findStartingPoint(head)

if start:
    print("Starting point:", start.data)
else:
    print("No Loop")