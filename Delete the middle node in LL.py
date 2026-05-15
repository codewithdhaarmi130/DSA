class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteMiddle(head):

    # Empty list or single node
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    # Find middle node
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete middle node
    prev.next = slow.next

    return head


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

newHead = deleteMiddle(head)

printList(newHead)