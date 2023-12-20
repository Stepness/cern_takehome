def _mountain_area(mountain: dict) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']

def _in_range_mountains_combinations(mountains: list, quantity: int):
    intersection_area = 0
    for index, mountain in enumerate(mountains): 
        temp_mountains = []
        temp_mountains.append(mountain)
        for j, next_mountain in enumerate(mountains[index+1:index+quantity]):
            if(mountain['right'] >= next_mountain['left']):
                temp_mountains.append(next_mountain)
        if len(temp_mountains) == quantity:
            intersection_area +=_intersection_area(temp_mountains)
    return intersection_area

def _remove_contained_mountains(mountains: list):
    for index in range(len(mountains) - 2, -1, -1):
        mountain = mountains[index]
        next_mountain = mountains[index + 1]
        if next_mountain['right'] <= mountain['right']:
            mountains.pop(index + 1)
    return mountains
 
def _intersection_area(mountains: list) -> float:
    rightmost_left = max(mountains, key=lambda x: x['left'])['left']
    leftmost_right = min(mountains, key=lambda x: x['right'])['right']
    
    intersection_base = leftmost_right - rightmost_left
    
    if intersection_base > 0:
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area
    return 0

def _inclusion_exclusion_principle(mountains: list) -> float:
    total_area = 0

    for mountain in mountains:
        total_area += _mountain_area(mountain)

    for index, _ in enumerate(mountains):
        if index > 0:
            sign = pow(-1, index)
            n_mountains_combinations = _in_range_mountains_combinations(mountains, index+1)
            current_row = sign * n_mountains_combinations
            total_area += current_row

    return total_area

def visible_area(mountains: list) -> float:
    sorted_mountains = sorted(mountains, key=lambda x: x['left'])
    useful_mountains = _remove_contained_mountains(sorted_mountains)
    return _inclusion_exclusion_principle(useful_mountains)

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

    # for i in range(MAXIMUM_QUANTITY_OF_MOUNTAINS):
    #     temp_mountain = {'left': 0, 'right': 6, 'height': 3}
    #     mountains.append(temp_mountain)

    mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 0, 'right':  6, 'height': 3},
    ]
    # for i in range(MAXIMUM_QUANTITY_OF_MOUNTAINS):
    #     temp_mountain = {'left': 0, 'right': 6, 'height': 3}
    #     temp_mountain['right'] = temp_mountain['right'] + i
    #     temp_mountain['left'] = temp_mountain['left'] + i
    #     mountains.append(temp_mountain)
    
    print(visible_area(mountains))