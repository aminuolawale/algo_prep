from typing import Sequence


def solution(build_runs: Sequence[Sequence[bool]]) -> int:
    build_health = map_to_percent(build_runs)
    running_count = 0
    global_count = 0
    for index, build in enumerate(build_health):
        if index > 0 and build < build_health[index - 1]:
            running_count += 1
        else:
            global_count = (
                running_count if global_count < running_count else global_count
            )
            running_count = 0
    return global_count


def map_to_percent(build_runs: Sequence[Sequence[bool]]) -> Sequence[float]:
    return [float(a.count(True) / len(a)) for a in build_runs]


build_runs = [
    [True, True, True, False, False],
    [True, True, True, True, False],
    [True, True, True, True, True, True, True, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True, True, True, True, False],
    [True, False],
    [True, True, True, True, False, False],
]
print(solution(build_runs))