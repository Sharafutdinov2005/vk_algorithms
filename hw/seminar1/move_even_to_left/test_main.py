from main import move_even


def test_sort():
    tmp = []
    move_even(tmp)
    assert tmp == []

    tmp = [0]
    move_even(tmp)
    assert tmp == [0]

    tmp = [1]
    move_even(tmp)
    assert tmp == [1]

    tmp = [0, 1]
    move_even(tmp)
    assert tmp == [0, 1]

    tmp = [1, 0]
    move_even(tmp)
    assert tmp == [0, 1]

    tmp = [1, 1, 0]
    move_even(tmp)
    assert tmp == [0, 1, 1]

    tmp = [1, 0, 1]
    move_even(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1]
    move_even(tmp)
    assert tmp == [0, 1, 1]

    tmp = [0, 1, 1, 0]
    move_even(tmp)
    assert tmp == [0, 0, 1, 1]

    tmp = [1, 2, 1, 4, 1, 6]
    move_even(tmp)
    assert tmp == [2, 4, 6, 1, 1, 1]
