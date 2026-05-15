class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detectLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        if slow == fast:
            return True

    return False


# Creating linked list
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth

# Creating loop
fourth.next = second

print(detectLoop(head))