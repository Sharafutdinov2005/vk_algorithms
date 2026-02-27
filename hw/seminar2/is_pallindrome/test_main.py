from main import is_pallindrome


def test_is_pall():
    assert is_pallindrome("aaa") is True
    assert is_pallindrome("aaaa") is True
    assert is_pallindrome("aaba") is False
    assert is_pallindrome("aabba") is False
