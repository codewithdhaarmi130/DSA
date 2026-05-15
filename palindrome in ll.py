class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def isPalindrome(head):

    if head is None or head.next is None:
        return True

    # Find middle
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    secondHalf = reverse(slow.next)

    # Compare both halves
    first = head
    second = secondHalf

    while second:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True


# Create linked list
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(2)
fifth = Node(1)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(isPalindrome(head))