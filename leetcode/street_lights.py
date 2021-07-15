from typing import List


def street_lights(street_light_data: List[List[int]], street_length: int) -> int:
    raw_street_light_ranges = [[a[0] - a[1], a[0] + a[1]] for a in street_light_data]
    street_light_ranges = sorted(raw_street_light_ranges, key=lambda a: a[0])
    current_position = 0
    farthest_reaching_light_range = [float("-inf"), float("-inf")]
    index = 0
    selected_lights = []
    while current_position < street_length and index < len(street_light_ranges):
        current_light_range = street_light_ranges[index]
        overlap = False
        while current_light_range[0] <= current_position:
            overlap = True
            if farthest_reaching_light_range[1] < current_light_range[1]:
                farthest_reaching_light_range = current_light_range
            index += 1
            if index >= len(street_light_ranges):
                break
            current_light_range = street_light_ranges[index]
        if not overlap:
            return -1
        selected_lights.append(
            [
                sum(farthest_reaching_light_range) // 2,
                (farthest_reaching_light_range[1] - farthest_reaching_light_range[0]) // 2,
            ]
        )
        current_position = farthest_reaching_light_range[1]
    if current_position < street_length:
        return -1
    return len(selected_lights), selected_lights


if __name__ == "__main__":
    sl = [[0, 5], [1, 3], [5, 4], [8, 3], [11, 5], [15, 6]]
    street_length = 20
    print(street_lights(sl, 10))
