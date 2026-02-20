from typing import List


def move_even(
    array: List[int]
) -> None:
    """
    Moves even nums into begining of array.
    """

    left, right = 0, len(array)-1

    while left < right:
        if array[left] % 2 == 1:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
