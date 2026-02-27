from main import delete_dublicates


def test_delete_dublicates():
    a = []
    delete_dublicates(a)
    assert a == []

    a = [0]
    delete_dublicates(a)
    assert a == [0]

    a = [0, 0]
    delete_dublicates(a)
    assert a == [0]

    a = [0, 0, 0, 0, 1]
    delete_dublicates(a)
    assert a == [0, 1]

    a = [0, 0, 0, 0, 1, 1, 1, 2]
    delete_dublicates(a)
    assert a == [0, 1, 2]

    a = [0, 0, 0, 0, 1, 1, 1, 2, 2]
    delete_dublicates(a)
    assert a == [0, 1, 2]
