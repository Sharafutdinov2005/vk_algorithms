from typing import Any, Iterable, Optional


class Node:
    """
    Implementation of one-linked list node.
    """

    value: Any
    next: Optional["Node"] = None

    def __init__(
        self,
        value: Any = None,
    ) -> None:
        """
        Builds a Node object.

        Args:
            value (Any, optional): object to keep in `.value`. Defaults to
            None.
        """
        self.value = value


class Stack:
    """
    Class implementing stack based on one-linked list.
    """

    _headguard: Node
    _head: Optional[Node] = None

    _lenght: int = 0

    def __init__(
        self,
        iterable: Optional[Iterable[Any]] = None
    ) -> None:
        """
        Builds one-linked list.

        Args:
            iterable (Optional[Iterable[Any]], optional): iterable object to
            convert into list. Defaults to None.

            Note: first element of iterable becomes top of stack.
        """
        self._headguard = Node()
        current = self._headguard

        if iterable is not None:
            for element in iterable:
                current.next = Node(element)
                current = current.next
                self._lenght += 1

        self._head = self._headguard.next

    @property
    def top(
        self,
    ) -> Any:
        """
        Returns value of top element in stack.

        Returns:
            Any: value in top of stack.
        """
        return None if self._head is None else self._head.value

    def push(
        self,
        value: Any
    ) -> None:
        current = Node(value)

        self._headguard.next, current.next = current, self._headguard.next

        self._head = self._headguard.next
        self._lenght += 1

    def pop(
        self,
    ) -> Any:
        if self._headguard.next is None:
            return None
        top = self.top

        self._headguard.next = self._headguard.next.next
        self._head = self._headguard.next
        self._lenght -= 1

        return top

    def __len__(
        self
    ) -> int:
        return self._lenght

    def __str__(
        self
    ) -> str:
        result = ""

        current = self._head

        while current is not None:
            result += str(current.value) + " "
            current = current.next

        return result


def is_string_source(
    string_source: str,
    string: str
) -> bool:
    stack = Stack(string_source)

    for elem in string:
        if stack.top == elem:
            stack.pop()

    print(stack)

    return len(stack) == 0
