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