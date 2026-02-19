from typing import List


def merge_arrays(
    arr1: List[int],
    arr2: List[int]
) -> List[int]:
    """
    Merges two lists in one new list. Takes two sorted in
    increasing order lists.
    """

    result = []
    ptr1 = ptr2 = 0

    while ptr1 < len(arr1) or ptr2 < len(arr2):
        # lazy logical op won't calculate 2nd comparation
        # if 1st true
        if ptr2 >= len(arr2) or ptr1 < len(arr1) and arr1[ptr1] < arr2[ptr2]:
            result.append(arr1[ptr1])
            ptr1 += 1
        else:
            result.append(arr2[ptr2])
            ptr2 += 1

    return result
