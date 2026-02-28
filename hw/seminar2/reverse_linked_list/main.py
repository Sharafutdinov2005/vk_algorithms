from typing import Any, Optional


class Node:
    value: Any
    next: Optional["Node"] = None

    def __init__(
        self,
        value: Any,
    ) -> None:
        self.value = value


def reverse_linked_list(
    head: Node,
) -> Node:
    if head.next is None:
        return head

    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev  # type: ignore
