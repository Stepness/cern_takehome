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
    rightmost_left = max(mountains, key=lambda x: x['left'])
    leftmost_right = min(mountains, key=lambda x: x['right'])
    
    intersection_base = leftmost_right - rightmost_left
    if(intersection_base > 0):
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area    
    return total_area

def lists_of_intersections(combinations_of_n_mountains: list):
    for list in combinations_of_n_mountains:
        intersection_of_n(list)

def PIE(mountains):
    total_area = 0
    for current_mountain in mountains:
        total_area += mountain_area(current_mountain)
    
    for index, mountain in enumerate(mountains):
        if(index > 1):
            total_area += (-1**(index+1)) * lists_of_intersections(combinations(mountains, index))
        
    return total_area
        

def main():
    mountains = [
        {'left': 9, 'right': 15, 'height': 3},
        {'left': 8, 'right': 14, 'height': 3},
        {'left': 0, 'right':  6, 'height': 3},
    ]

    
    #result = visible_area(mountains)
    #print("Visible Area:", result)
    var = PIE(mountains)
    print(var)

if __name__ == "__main__":
    main()