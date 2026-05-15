class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeNthFromEnd(head, n):

    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast n+1 steps
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next


def printList(head):

    while head:
        print(head.data, end=" ")
        head = head.next


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

n = 2

newHead = removeNthFromEnd(head, n)

printList(newHead)