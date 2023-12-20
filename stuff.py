def _in_range_mountains_combinations(mountains: list, quantity: int):
    locations = {}
    result_mountains = []
    for mountain in mountains:
        left = mountain['left']
        right = mountain['right']
        for i in range(right-left):
            locations[left+i] = locations.get(left+i, 0) + 1
    
    for mountain in mountains:
        left = mountain['left']
        right = mountain['right']
        
        # Check if the base of the mountain is in locations and appeared quantity times
        if all(locations.get(left + i, 0) >= quantity for i in range(right - left)):
            result_mountains.append(mountain)
    
    return itertools.combinations(result_mountains, quantity)