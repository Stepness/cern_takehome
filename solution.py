import itertools


def _mountain_area(mountain: dict) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']


def _intersection_area(mountains: list) -> float:
    rightmost_left = max(mountains, key=lambda x: x['left'])['left']
    leftmost_right = min(mountains, key=lambda x: x['right'])['right']

    intersection_base = leftmost_right - rightmost_left

    if intersection_base > 0:
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area
    return 0


def _overlapping_mountains(current_mountain_index: int, mountains: list) -> list:
    overlapping_mountains = []
    current_mountain = mountains[current_mountain_index]

    for following_mountain in mountains[current_mountain_index+1:]:
        if current_mountain['right'] >= following_mountain['left']:
            overlapping_mountains.append(following_mountain)
        else:
            break
    return overlapping_mountains


def _mountain_intersections(current_mountain_index: int, mountains: list) -> float:
    total_intersection_area = 0

    overlapping_mountains = []
    overlapping_mountains = _overlapping_mountains(current_mountain_index, mountains)

    if overlapping_mountains:
        for i in range(1, len(overlapping_mountains) + 1):
            combinations = list(itertools.combinations(overlapping_mountains, i))
            for intersected_mountains_combination in combinations:
                current_mountain = mountains[current_mountain_index]
                current_mountain_intersection = list(intersected_mountains_combination) + [current_mountain]
                sign = pow(-1, i)
                intersection_area = sign * _intersection_area(current_mountain_intersection)
                total_intersection_area += intersection_area

    return total_intersection_area


def remove_nested_mountains(mountains: list) -> list:
    for index in range(len(mountains) - 2, -1, -1):
        mountain = mountains[index]
        next_mountain = mountains[index + 1]
        if next_mountain['right'] <= mountain['right']:
            mountains.pop(index + 1)
    return mountains


def inclusion_exclusion_principle(mountains: list) -> float:
    total_area = 0

    for index, mountain in enumerate(mountains):
        total_area += _mountain_area(mountain)
        total_area += _mountain_intersections(index, mountains)

    return total_area


def visible_area(mountains: list) -> float:
    sorted_mountains = sorted(mountains, key=lambda x: x['left'])
    non_nested_mountains = remove_nested_mountains(sorted_mountains)
    return inclusion_exclusion_principle(non_nested_mountains)
