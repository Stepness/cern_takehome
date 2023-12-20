import itertools
    
def mountain_area(mountain: dict) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']

def intersection_of_n(mountains: list) -> float:
    total_area = 0
    rightmost_left = max(mountains, key=lambda x: x['left'])['left']
    leftmost_right = min(mountains, key=lambda x: x['right'])['right']
    
    intersection_base = leftmost_right - rightmost_left
    if(intersection_base > 0):
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area
    return total_area

def sum_of_intersections(combinations_of_n_mountains: list) -> float:
    sum = 0
    for mountains in combinations_of_n_mountains:
        sum += intersection_of_n(mountains)
    return sum

def inclusion_exclusion_principle(mountains: list) -> float:
    total_area = 0
    for current_mountain in mountains:
        total_area += mountain_area(current_mountain)

    for index, mountain in enumerate(mountains):
        if index > 0:
            exponent = pow(-1, index)
            combinations = itertools.combinations(mountains, index+1)
            current_row = exponent * sum_of_intersections(combinations)
            total_area += current_row

    return total_area

def visible_area(mountains: list) -> float:
    return inclusion_exclusion_principle(mountains)

def main():
    mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 0, 'right':  6, 'height': 3},
]
    res = visible_area(mountains)
    print(res)

if __name__ == "__main__":
    main()
    