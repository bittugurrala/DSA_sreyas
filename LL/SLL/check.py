class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


def conqure(head1, head2):
    dummy = Node(None)
    tail = dummy

    while head1 and head2:
        if head1.value < head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    if head2:
        tail.next = head2

    return dummy.next


array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

list1 = LinkedList()
for i in array1:
    list1.append(i)

list2 = LinkedList()
for i in array2:
    list2.append(i)

res = conqure(list1.head, list2.head)

current = res
while current:
    print(current.value, end=" ")
    current = current.next
