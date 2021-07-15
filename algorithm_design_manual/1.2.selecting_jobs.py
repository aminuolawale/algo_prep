"""
Movie Scheduling problem:
Given a set of movie shoots (represented with start and end times) find the largest set of non overlapping movie shoots
"""
"""
Algorithm:
-Iterate through the intervals sorted by their start times in ascending order
-Keep the interval with the earliest start time through the iteration
-If we encounter an interval with a start time later than the stored interval's end time, we append the stored interval to our list of chosen intervals and store the 
current interval.
-Keep the interval with the earliest start time through the iteration and repeat the previous steps till the end of the list
"""




from typing import Tuple, List
def schedule(shoots: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    O(n) -> 
    """
    shoots = sorted(shoots, key=lambda a: a[0])
    result = []
    current_shoot = [None, None]
    for s in shoots:
        if current_shoot[0] is None or s[1] < current_shoot[1]:
            current_shoot = s
        elif current_shoot[1] <= s[0]:
            result.append(current_shoot)
            current_shoot = s
    result.append(current_shoot)
    return result


if __name__ == "__main__":
    shoots = [
        (0, 3), (1, 2), (1, 4), (2,
                                 5), (2, 4), (2, 3), (3, 4), (2, 6), (4, 5), (4, 6), (5, 7)
    ]
    result = schedule(shoots)
    print(result)
