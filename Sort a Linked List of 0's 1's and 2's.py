class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sort012(head):

    # Dummy nodes
    zeroD = Node(-1)
    oneD = Node(-1)
    twoD = Node(-1)

    # Tails
    zero = zeroD
    one = oneD
    two = twoD

    curr = head

    # Separate nodes
    while curr:

        if curr.data == 0:
            zero.next = curr
            zero = zero.next

        elif curr.data == 1:
            one.next = curr
            one = one.next

        else:
            two.next = curr
            two = two.next

        curr = curr.next

    # Connect lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    # New head
    head = zeroD.next

    return head


def printList(head):

    while head:
        print(head.data, end=" ")
        head = head.next


# Create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)

sortedHead = sort012(head)

printList(sortedHead)