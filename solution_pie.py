def combinations(lst, n):
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        remainlst_combo = combinations(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
           
    return l

def mountain_area(mountain) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']

def intersection_of_n(mountains: list):
    total_area = 0
    rightmost_left = max(mountains, key=lambda x: x['left'])['left']
    leftmost_right = min(mountains, key=lambda x: x['right'])['right']
    
    intersection_base = leftmost_right - rightmost_left
    if(intersection_base > 0):
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area
    return total_area

def sum_of_intersections(combinations_of_n_mountains: list):
    sum = 0
    for mountains in combinations_of_n_mountains:
        sum += intersection_of_n(mountains)
    return sum

def PIE(mountains):
    total_area = 0
    for current_mountain in mountains:
        total_area += mountain_area(current_mountain)
    
    for index, mountain in enumerate(mountains):
        if(index > 0):
            exponent = pow(-1, index)
            current_row = exponent * sum_of_intersections(combinations(mountains, index+1))
            total_area += current_row
            
    return total_area
        

def main():
    # mountains = [
    #     {'left': 0, 'right': 6, 'height': 3},
    #     {'left': 0, 'right':  6, 'height': 3},
    #     {'left': 20, 'right':  30, 'height': 10},
    # ]
    mountains = [
        {'left': 0, 'right': 6, 'height': 3},
        {'left': 0, 'right': 6, 'height': 3},
        {'left': 4, 'right':  6, 'height': 1},
    ]
    
    var = PIE(mountains)
    print(var)

if __name__ == "__main__":
    main()