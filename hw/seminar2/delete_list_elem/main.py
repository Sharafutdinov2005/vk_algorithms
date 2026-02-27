from typing import Any, Optional


class Node:
    value: Any
    next: Optional["Node"] = None

    def __init__(
        self,
        value: Any,
    ) -> None:
        self.value = value


def delete_list_element(
    head: Node,
    value: Any,
) -> Node:
    headguard = Node(None)
    headguard.next = head
    prev = headguard
    curr = head

    while curr is not None:
        if curr.value == value:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

    return headguard.next
