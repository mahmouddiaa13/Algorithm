from typing import List
def merge_sort(arr: List[int]) -> None:
    """ f(n) = O(nlog(n)) as n-> infinity """

    if len(arr) > 1:
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k =0
        while(i < len(left_arr) and j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = right_arr[j]
                k += 1
                j += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3]
    merge_sort(arr)
    print(arr)
