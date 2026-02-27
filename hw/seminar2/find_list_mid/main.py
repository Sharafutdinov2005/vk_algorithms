from typing import Any, Optional


class Node:
    value: Any
    next: Optional["Node"] = None

    def __init__(
        self,
        value: Any,
    ) -> None:
        self.value = value


def find_list_mid(
    head: Node,
) -> Node:
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
