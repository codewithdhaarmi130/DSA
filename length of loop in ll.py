class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthOfLoop(head):
    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Count loop length
            count = 1
            temp = slow.next

            while temp != slow:
                count += 1
                temp = temp.next

            return count

    return 0


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

print("Length of loop:", lengthOfLoop(head))