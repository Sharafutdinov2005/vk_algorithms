from main import merge_arrays


def test_merge_edge_cases():
    assert merge_arrays([], []) == []
    assert merge_arrays([1], []) == [1]
    assert merge_arrays([], [1]) == [1]
    assert merge_arrays([1], [0]) == [0, 1]


def test_merge():
    assert merge_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_arrays([1, 1, 5], [2, 4, 6]) == [1, 1, 2, 4, 5, 6]
