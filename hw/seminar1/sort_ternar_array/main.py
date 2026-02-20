from typing import List


def sort_ternary(
    array: List[int],
) -> None:
    """
    Sorts array of 0, 1, 3.
    """
    left, mid, right = 0, 0, len(array)-1

    while mid <= right:
        if array[mid] == 0:
            array[left], array[mid] = array[mid], array[left]
            left += 1
        elif array[mid] == 2:
            array[right], array[mid] = array[mid], array[right]
            right -= 1
        elif array[mid] != 1:
            raise ValueError("element not in {0, 1, 2}!")
        mid += 1
