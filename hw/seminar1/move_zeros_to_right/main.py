from typing import List


def move_zeros(
    array: List[int]
) -> None:
    """
    Moves 0 into end of array.
    """

    left, right = 0, len(array)-1

    while left < right:
        if array[left] == 0:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
