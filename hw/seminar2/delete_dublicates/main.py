from typing import List


def delete_dublicates(
    numbers: List[int]
) -> None:
    slow, fast = 0, 1

    while fast < len(numbers):
        if numbers[slow] != numbers[fast]:
            numbers[slow + 1] = numbers[fast]
            slow += 1
        fast += 1

    while slow < len(numbers) - 1:
        numbers.pop()  # O(1) for last elem
