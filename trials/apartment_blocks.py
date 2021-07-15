from typing import Sequence, Mapping


def solution(blocks: Mapping[str, int], reqs: Sequence[str]) -> int:
    min_count = float("inf")
    min_index = -1
    for index, b in enumerate(blocks):
        b_keys = [a for a in b.keys() if b[a]]
        if set(b_keys) == set(reqs):
            return index
        else:
            seen_buildings = set(b_keys)
            j = index + 1
            k = index - 1
            step = 0
            while k > -1 or j < len(blocks):
                step += 1
                seen_buildings = set()
                if k > -1:
                    bk_keys = [a for a in blocks[k].keys() if blocks[k][a]]
                    seen_buildings = seen_buildings.union(set(bk_keys))
                if j < len(blocks):
                    bj_keys = [a for a in blocks[j].keys() if blocks[j][a]]
                    seen_buildings = seen_buildings.union(set(bj_keys))
                if seen_buildings == set(reqs):
                    if min_count > step:
                        print(min_count, index, step)
                        min_count = step
                        min_index = index
                j += 1
                k -= 1
    return min_index


blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

print(solution(blocks, reqs))