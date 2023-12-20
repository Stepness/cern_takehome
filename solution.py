import itertools
    
def _mountain_area(mountain: dict) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']

def _in_range_mountains_combinations(mountains: list, quantity: int):
    mountains_to_combine = []
    
    for i, current_mountain in enumerate(mountains):
        temp_overlapping_mountains = []
        temp_overlapping_mountains.append(current_mountain)
        for _, next_mountain in enumerate(mountains[i:]):
            if current_mountain['right'] >= next_mountain['left']:
                temp_overlapping_mountains.append(next_mountain)
                if len(temp_overlapping_mountains) >= quantity:
                    for new_dict in temp_overlapping_mountains:
                        if new_dict not in mountains_to_combine:
                            mountains_to_combine.append(new_dict)
            
    return itertools.combinations(mountains_to_combine, quantity)

def _remove_contained_mountains(mountains: list):
    for index in range(len(mountains) - 2, -1, -1):
        mountain = mountains[index]
        next_mountain = mountains[index + 1]
        if next_mountain['right'] <= mountain['right']:
            mountains.pop(index + 1)
    return mountains
 
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
    sorted_mountains = sorted(mountains, key=lambda x: x['left'])
    useful_mountains = _remove_contained_mountains(sorted_mountains)
    
    for mountain in useful_mountains:
        total_area += _mountain_area(mountain)

    for index, _ in enumerate(useful_mountains):
        if index > 0:
            print(index)
            sign = pow(-1, index)
            n_mountains_combinations = _in_range_mountains_combinations(useful_mountains, index+1)
            current_row = sign * _intersections_summation(n_mountains_combinations)
            total_area += current_row

    return total_area

def visible_area(mountains: list) -> float:
    return _inclusion_exclusion_principle(mountains)

if __name__ == '__main__':
    MAXIMUM_QUANTITY_OF_MOUNTAINS = 1000
    mountain = {'left': 0, 'right': 6, 'height': 3}
    mountains = []
    # mountains = [
    # {'left': 0, 'right': 10, 'height': 5},
    # {'left': 1, 'right': 11, 'height': 5},
    # {'left': 2, 'right': 12, 'height': 5},
    # {'left': 2, 'right': 12, 'height': 5},
    # {'left': 2, 'right': 12, 'height': 5},
    # {'left': 3, 'right': 12, 'height': 4.5},
    # {'left': 3, 'right': 13, 'height': 5},
    # ]
    
#     mountains = [
#     {'left': 9, 'right': 15, 'height': 3},
#     {'left': 8, 'right': 14, 'height': 3},
#     {'left': 0, 'right':  6, 'height': 3},
# ]

    for i in range(MAXIMUM_QUANTITY_OF_MOUNTAINS):
        temp_mountain = {'left': 0, 'right': 6, 'height': 3}
        temp_mountain['right'] = temp_mountain['right'] + i
        temp_mountain['left'] = temp_mountain['left'] + i
        mountains.append(temp_mountain)
    
    print(visible_area(mountains))