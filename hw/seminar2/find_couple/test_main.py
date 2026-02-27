from main import find_couple


def test_find_couple():
    assert find_couple([], 4) is False
    assert find_couple([1], 4) is False
    assert find_couple([1, 1], 4) is False
    assert find_couple([2, 2], 4) is True
    assert find_couple([0, 0, 1, 2, 3, 5], 4) is True
