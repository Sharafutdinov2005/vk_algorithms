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

    tmp = [1, 1, 0]
    move_zeros(tmp)
    assert tmp == [1, 1, 0]

    tmp = [1, 0, 1]
    move_zeros(tmp)
    assert tmp == [1, 1, 0]

    tmp = [0, 1, 1]
    move_zeros(tmp)
    assert tmp == [1, 1, 0]
    tmp = [0, 1, 1, 0]
    move_zeros(tmp)
    assert tmp == [1, 1, 0, 0]
