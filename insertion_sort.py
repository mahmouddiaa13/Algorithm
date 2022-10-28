from typing import List


def sort_list(data: List[int]) -> List[int]:
    """ f(n) = O(n^2) as n-> infinity """

    for i in range(1, len(data)):
        item = data[i]
        j = i-1
        while j >= 0 and data[j] > item:
                data[j+1] = data[j]
                j -=1
        data[j+1] = item
    return data


if __name__ == "__main__":
    print(sort_list([9, 5, 1, 4, 3]))