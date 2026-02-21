from main import move_zeros


def test_sort():
    tmp = []
    move_zeros(tmp)
    assert tmp == []

    tmp = [0]
    move_zeros(tmp)
    assert tmp == [0]

    tmp = [1]
    move_zeros(tmp)
    assert tmp == [1]

    tmp = [0, 1]
    move_zeros(tmp)
    assert tmp == [1, 0]

    tmp = [1, 0]
    move_zeros(tmp)
    assert tmp == [1, 0]

    tmp = [2, 1, 0]
    move_zeros(tmp)
    assert tmp == [2, 1, 0]

    tmp = [2, 0, 1]
    move_zeros(tmp)
    assert tmp == [2, 1, 0]

    tmp = [0, 2, 1]
    move_zeros(tmp)
    assert tmp == [2, 1, 0]

    tmp = [0, 2, 1, 0]
    move_zeros(tmp)
    assert tmp == [2, 1, 0, 0]

    tmp = [1, 0, 2, 0, 3, 0, 4]
    move_zeros(tmp)
    assert tmp == [1, 2, 3, 4, 0, 0, 0]

    tmp = [0, 2, 0, 3, 0]
    move_zeros(tmp)
    assert tmp == [2, 3, 0, 0, 0]
