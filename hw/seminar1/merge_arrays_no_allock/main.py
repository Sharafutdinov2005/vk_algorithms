from typing import List


def merge_arrays_no_allock(
    src: List[int],
    dest: List[int]
) -> None:

    if len(src) > len(dest):
        raise ValueError("there is no space in dest!")

    ptr_src, ptr_dest = len(src)-1, len(dest)-len(src)-1
    ptr = len(dest)-1

    while ptr_src >= 0:
        if ptr_dest < 0 or src[ptr_src] >= dest[ptr_dest]:
            dest[ptr] = src[ptr_src]
            ptr_src -= 1
        else:
            dest[ptr] = dest[ptr_dest]
            ptr_dest -= 1
        ptr -= 1
