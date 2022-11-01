from typing import List


def binary_search(arr: List[int], item: int) -> int:
    """f(n) = O(log(n)) as n-> infinity"""

    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = (high + low) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    print(binary_search([0, 5, 6, 9, 11, 20], 21))
