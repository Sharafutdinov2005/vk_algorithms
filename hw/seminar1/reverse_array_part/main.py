from typing import Any, List, Optional


def reverse_array(
    array: List[Any],
    start: Optional[int] = None,
    end: Optional[int] = None
) -> None:
    """
    Reverses array elements order from start to end. Start and end
    must be in range from 0 to n, and start must be less, than end.
    """

    start = 0 if start is None else start
    end = len(array) if end is None else end

    if len(array) == 0:
        raise ValueError("array is empty!")
    if start < 0 or start >= len(array):
        raise ValueError("start is out of range!")
    if end < 0 or end > len(array):
        raise ValueError("end is out of range!")
    if start >= end:
        raise ValueError("start can't be equal or greater than end!")

    while start < end:
        array[start], array[end-1] = array[end-1], array[start]
        start += 1
        end -= 1


def reverse_array_part(
    array: List[Any],
    k: int,
) -> None:
    """
    Makes cycle move of array on k elements from right to left.
    k must be positive number, array mustn't be empty.
    """

    if len(array) == 0:
        raise ValueError("array is empty!")
    if k < 0:
        raise ValueError("k can't be negative!")

    k %= len(array)

    reverse_array(array)
    reverse_array(array, end=k)
    reverse_array(array, start=k)
