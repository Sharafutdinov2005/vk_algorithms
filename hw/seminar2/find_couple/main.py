from typing import List


def find_couple(
    numbers: List[int],
    target: int
) -> bool:
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return True
        if numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

    return False
