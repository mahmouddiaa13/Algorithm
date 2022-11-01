from typing import List


def segregate(arr: List[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        segregate(left_arr)
        segregate(right_arr)

        i = j = k = 0
        while i < len(left_arr) and left_arr[i] < 0:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr) and right_arr[j] < 0:
            arr[k] = right_arr[j]
            j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [-1, 9, -5, -20, 5, -3, 1, 4, 0, 3]
    segregate(arr)
    print(arr)
