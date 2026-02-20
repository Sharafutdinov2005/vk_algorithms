from main import merge_arrays_no_allock


def test_merge_arrays_edge_cases():
    tmp = []
    merge_arrays_no_allock([], tmp)
    assert tmp == []

    tmp = [0]
    merge_arrays_no_allock([], tmp)
    assert tmp == [0]

    tmp = [0]
    merge_arrays_no_allock([0], tmp)
    assert tmp == [0]  # it thinks, that zero in tmp is free space


def test_merge_arrays():
    tmp = [1, 2, 0]
    merge_arrays_no_allock([5], tmp)
    assert tmp == [1, 2, 5]

    tmp = [1, 5, 0]
    merge_arrays_no_allock([2], tmp)
    assert tmp == [1, 2, 5]

    tmp = [2, 5, 0]
    merge_arrays_no_allock([1], tmp)
    assert tmp == [1, 2, 5]

    tmp = [2, 4, 5, 0, 0, 0, 0]
    merge_arrays_no_allock([-1, 1, 3, 6], tmp)
    assert tmp == [-1, 1, 2, 3, 4, 5, 6]
