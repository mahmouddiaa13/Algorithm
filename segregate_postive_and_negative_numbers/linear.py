from typing import List


def segregate(array: List[int]) -> List[int]:
    positive_list = list()
    result = list()
    for item in array:
        if item < 0:
            result.append(item)
        else:
            positive_list.append(item)
    result.extend(positive_list)
    return result


if __name__ == "__main__":
    arr = [-1, 9, -5, -20, 5, -3, 1, 4, 0, 3]
    print(segregate(arr))
