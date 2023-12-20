import itertools
    
def _mountain_area(mountain: dict) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']

def _areas_intersection(mountains: list) -> float:
    rightmost_left = max(mountains, key=lambda x: x['left'])['left']
    leftmost_right = min(mountains, key=lambda x: x['right'])['right']
    
    intersection_base = leftmost_right - rightmost_left
    
    if intersection_base > 0:
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area
    return 0

def _intersections_summation(mountains_combinations: list) -> float:
    summation = 0
    for mountains_combination in mountains_combinations:
        summation += _areas_intersection(mountains_combination)
    return summation

def _inclusion_exclusion_principle(mountains: list) -> float:
    total_area = 0
    for mountain in mountains:
        total_area += _mountain_area(mountain)

    for index, _ in enumerate(mountains):
        if index > 0:
            print(index)
            sign = pow(-1, index)
            n_mountains_combinations = itertools.combinations(mountains, index+1)
            current_row = sign * _intersections_summation(n_mountains_combinations)
            total_area += current_row

    return total_area

def visible_area(mountains: list) -> float:
    return _inclusion_exclusion_principle(mountains)
