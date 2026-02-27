from main import Node, find_list_mid


def test_find_list_mid():
    head = Node(1)
    mid1 = Node(2)
    mid2 = Node(3)
    tail = Node(4)

    assert find_list_mid(head) == head

    head.next = mid1

    assert find_list_mid(head) == mid1

    mid1.next = mid2

    assert find_list_mid(head) == mid1

    mid2.next = tail

    assert find_list_mid(head) == mid2
