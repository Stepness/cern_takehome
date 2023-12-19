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
    
def intersection_of_2(first_mountain, second_mountain):
    rightmost_left = max(first_mountain['left'], second_mountain['left'])
    leftmost_right = min(first_mountain['right'], second_mountain['right'])
    intersection_base = leftmost_right - rightmost_left
    if(intersection_base > 0):
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area    
    return 0

def intersection_of_n(mountains):
    total_area = 0
    rightmost_left = max(mountains, key=lambda x: x['left'])
    leftmost_right = min(mountains, key=lambda x: x['right'])
    
    intersection_base = leftmost_right - rightmost_left
    if(intersection_base > 0):
        intersection_height = 0.5 * intersection_base
        intersection_area = 0.5 * intersection_base * intersection_height
        return intersection_area    
    return total_area
    
def PIE(mountains):
    total_area = 0
    for current_mountain in mountains:
        total_area += mountain_area(current_mountain)
    
    for index, mountain in enumerate(mountains):
        combinations(mountains, index)
        

def main():
    mountains = [
        {'left': 9, 'right': 15, 'height': 3},
        {'left': 8, 'right': 14, 'height': 3},
        {'left': 0, 'right':  6, 'height': 3},
    ]

    
    #result = visible_area(mountains)
    #print("Visible Area:", result)
    var = combinations(mountains, 1)
    print(var)

if __name__ == "__main__":
    main()