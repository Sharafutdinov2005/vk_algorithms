from typing import List


def move_zeros(
    array: List[int]
) -> None:
    """
    Moves 0 into end of array.
    """

    ptr_positive, ptr = 0, 0

    while ptr < len(array):
        if array[ptr] != 0:
            array[ptr_positive], array[ptr] = array[ptr], array[ptr_positive]
            ptr_positive += 1
        ptr += 1
