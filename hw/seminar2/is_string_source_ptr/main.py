def is_string_source(
    string_source: str,
    string: str
) -> bool:
    ptr = 0

    for elem in string:
        if len(string_source) == ptr:
            break
        if string_source[ptr] == elem:
            ptr += 1

    return len(string_source) == ptr
