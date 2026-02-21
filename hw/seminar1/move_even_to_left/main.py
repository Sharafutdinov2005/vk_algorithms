from typing import List


def move_even(
    array: List[int]
) -> None:
    """
    Moves even nums into begining of array.
    """

    ptr_even, ptr = 0, 0

    while ptr < len(array):
        if array[ptr] % 2 == 0:
            array[ptr_even], array[ptr] = array[ptr], array[ptr_even]
            ptr_even += 1
        ptr += 1
