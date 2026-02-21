from main import sort_ternary


def test_sort():
    tmp = []
    sort_ternary(tmp)
    assert tmp == []

    tmp = [0]
    sort_ternary(tmp)
    assert tmp == [0]

    tmp = [1]
    sort_ternary(tmp)
    assert tmp == [1]

    tmp = [0, 1]
    sort_ternary(tmp)
    assert tmp == [0, 1]

    tmp = [1, 0]
    sort_ternary(tmp)
    assert tmp == [0, 1]

    tmp = [1, 1, 0]
    sort_ternary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [1, 0, 1]
    sort_ternary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1]
    sort_ternary(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1, 0]
    sort_ternary(tmp)
    assert tmp == [0, 0, 1, 1]

    tmp = [2, 1, 0]
    sort_ternary(tmp)
    assert tmp == [0, 1, 2]

    tmp = [2, 0, 1]
    sort_ternary(tmp)
    assert tmp == [0, 1, 2]

    tmp = [0, 2, 1]
    sort_ternary(tmp)
    assert tmp == [0, 1, 2]

    tmp = [2, 0, 1, 0]
    sort_ternary(tmp)
    assert tmp == [0, 0, 1, 2]
