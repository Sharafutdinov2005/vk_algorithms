from main import sort_binary


def test_sort():
    tmp = []
    sort_binary(tmp)
    assert tmp == []

    tmp = [0]
    sort_binary(tmp)
    assert tmp == [0]

    tmp = [1]
    sort_binary(tmp)
    assert tmp == [1]

    tmp = [0, 1]
    sort_binary(tmp)
    assert tmp == [0, 1]

    tmp = [1, 0]
    sort_binary(tmp)
    assert tmp == [0, 1]

    tmp = [1, 1, 0]
    sort_binary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [1, 0, 1]
    sort_binary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1]
    sort_binary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1, 0]
    sort_binary(tmp)
    assert tmp == [0, 0, 1, 1]
