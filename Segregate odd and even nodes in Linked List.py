class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def segregateEvenOdd(head):

    if head is None:
        return head

    evenStart = evenEnd = None
    oddStart = oddEnd = None

    curr = head

    while curr:

        # Even node
        if curr.data % 2 == 0:

            if evenStart is None:
                evenStart = evenEnd = curr
            else:
                evenEnd.next = curr
                evenEnd = evenEnd.next

        # Odd node
        else:

            if oddStart is None:
                oddStart = oddEnd = curr
            else:
                oddEnd.next = curr
                oddEnd = oddEnd.next

        curr = curr.next

    # If no even or odd nodes
    if evenStart is None or oddStart is None:
        return head

    # Connect even list with odd list
    evenEnd.next = oddStart
    oddEnd.next = None

    return evenStart


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
head.next.next.next.next.next = Node(6)

newHead = segregateEvenOdd(head)

printList(newHead)