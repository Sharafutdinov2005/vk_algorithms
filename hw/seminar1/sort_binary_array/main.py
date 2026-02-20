from typing import List


def sort_binary(
    array: List[int]
) -> None:
    """
    Sorts list of 1 and 0.
    """

    left, right = 0, len(array)-1

    while left < right:
        if (
            array[left] and array[left] != 1 or
            array[right] and array[right] != 1
        ):
            raise ValueError("there is non-binary value in array!")
        elif array[left] == 1:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
