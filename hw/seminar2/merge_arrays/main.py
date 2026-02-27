from typing import Iterable, Optional, Union, overload


class Node:
    value: int
    next: Optional["Node"] = None

    def __init__(
        self,
        value: int,
    ) -> None:
        self.value = value


class OneLinkedList:
    _headguard: Node = Node(0)
    _head: Optional[Node] = None
    _tail: Node

    _lenght: int = 0

    @overload
    def __init__(
        self,
        list_material: Optional[Iterable[int]] = None
    ) -> None: ...

    @overload
    def __init__(
        self,
        list_material: Node
    ) -> None: ...

    def __init__(
        self,
        list_material: Union[Node, Iterable[int], None] = None
    ) -> None:
        if isinstance(list_material, Node):
            self._head = list_material
            curr = self._head

            while curr.next is not None:
                curr = curr.next
                self._lenght += 1

            self._tail = curr
            return

        curr = self._headguard
        prev = self._headguard

        if list_material is not None:
            for elem in list_material:
                curr.next = Node(elem)
                prev = curr
                curr = curr.next
                self._lenght += 1

        self._head = self._headguard.next
        self._tail = prev

    @property
    def head(
        self
    ) -> int:
        if self._head is None:
            raise RuntimeError("List is empty!")
        return self._head.value

    def pop_front(
        self,
    ) -> Node:
        if self._head is None:
            raise RuntimeError("List is empty!")
        popped_head = self._head

        self._headguard.next = self._head.next
        self._head = self._headguard.next
        self._lenght -= 1

        return popped_head

    def push_back(
        self,
        node: Node,
    ) -> None:
        self._tail.next = node
        self._tail = node
        self._lenght += 1

    def __len__(
        self
    ) -> int:
        return self._lenght

    def __eq__(
        self,
        value: object
    ) -> bool:

        if isinstance(value, OneLinkedList):
            ptr1 = self._head
            ptr2 = value._head
            while ptr1 and ptr2:
                if ptr1.value != ptr2.value:
                    return False
                ptr1, ptr2 = ptr1.next, ptr2.next
            return ptr1 is None and ptr2 is None

        return NotImplemented()


def merge_lists(
    list1: OneLinkedList,
    list2: OneLinkedList
) -> OneLinkedList:
    result = OneLinkedList()

    while (len(list1) > 0) or (len(list2) > 0):
        if len(list1) <= 0 or len(list2) > 0 and list2.head < list2.head:
            result.push_back(list2.pop_front())
        else:
            result.push_back(list1.pop_front())

    return result
