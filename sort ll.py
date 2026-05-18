class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findMiddle(head):

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(left, right):

    dummy = Node(0)
    tail = dummy

    while left and right:

        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    if left:
        tail.next = left

    if right:
        tail.next = right

    return dummy.next


def mergeSort(head):

    if head is None or head.next is None:
        return head

    # Find middle
    mid = findMiddle(head)

    rightHead = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(rightHead)

    return merge(left, right)


def printList(head):

    while head:
        print(head.data, end=" ")
        head = head.next


# Create linked list
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

sortedHead = mergeSort(head)

printList(sortedHead)