from main import reverse_linked_list, Node


def test_reverse_linked_list():
    head = Node(1)
    mid = Node(2)
    tail = Node(3)

    assert reverse_linked_list(head) == head

    head.next = tail

    assert reverse_linked_list(head) == tail
    assert tail.next == head
    assert head.next is None

    head.next = mid
    mid.next = tail
    tail.next = None

    assert reverse_linked_list(head) == tail
    assert tail.next == mid
    assert mid.next == head
    assert head.next is None
