from main import Node, delete_list_element


def test_delete_list_element():
    head = Node(1)
    mid1 = Node(2)
    mid2 = Node(3)
    tail = Node(4)

    head.next = mid1
    mid1.next = mid2
    mid2.next = tail

    assert delete_list_element(head, 1) == mid1
    assert mid1.next == mid2
    assert mid2.next == tail

    assert delete_list_element(mid1, 3) == mid1
    assert mid1.next == tail
