from main import reverse_array, reverse_array_part


def test_reverse_array():
    temp = [i for i in range(5)]  # [0, 1, 2, 3, 4]

    # default
    reverse_array(temp)
    assert temp == [4, 3, 2, 1, 0]

    # inside part
    reverse_array(temp, start=1, end=4)
    assert temp == [4, 1, 2, 3, 0]


def test_reverse_array_part():
    default = [1, 2, 3, 4, 5, 6, 7]
    reverse_array_part(default, 3)
    assert default == [5, 6, 7, 1, 2, 3, 4]

    # multiple cycles
    temp = [i for i in range(5)]  # [0, 1, 2, 3, 4]
    reverse_array_part(temp, 5 + 3)
    assert temp == [2, 3, 4, 0, 1]
