from main import merge_lists, OneLinkedList


def test_merge_lists():
    empty1 = OneLinkedList()
    empty2 = OneLinkedList([])
    empty_result = OneLinkedList()

    assert merge_lists(empty1, empty2) == empty_result

    list1 = OneLinkedList([1, 1, 3, 5, 7, 9])
    list2 = OneLinkedList([2, 4, 4, 6, 8, 8])
    result = OneLinkedList([1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9])

    assert merge_lists(list1, list2) == result
