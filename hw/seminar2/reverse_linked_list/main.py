from typing import Any, Optional


class Node:
    value: Any
    next: Optional["Node"] = None

    def __init__(
        self,
        value: Any,
    ) -> None:
        self.value = value

    def __str__(
        self,
    ) -> str:
        curr = self
        values = ""

        while curr is not None:
            values += str(curr.value)
            curr = curr.next

        return values


def reverse_linked_list(
    head: Node,
) -> Node:
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
