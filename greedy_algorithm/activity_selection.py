from typing import List


def select_activities(activity_start: List[int], activity_end: List[int]) -> List[int]:
    """
    assuming the activities are already sorted according to their end time
    """
    result = [0]
    j = 0
    for i in range(1, len(activity_start)):

        if activity_end[j] <= activity_start[i]:
            result.append(i)
            j = i

    return result


if __name__ == "__main__":
    start = [9, 10, 11, 12, 13, 15]
    end = [11, 11, 12, 14, 15, 16]
    print(select_activities(start, end))
