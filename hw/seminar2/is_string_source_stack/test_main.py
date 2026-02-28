from main import is_string_source


def test_is_string_source():
    a = "Hello, World!!!!"
    b = "Hll, Wrld"

    assert is_string_source(b, a) is True
    assert is_string_source(a, b) is False
