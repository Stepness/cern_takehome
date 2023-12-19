def mountain_area(mountain) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']
    

def visible_area(mountains: list) -> float:
    visible_area = 0
    for index, current_mountain in enumerate(mountains):
        current_mountain_area = mountain_area(current_mountain)
        
        for previous_mountain in mountains[:index]:
            rightmost_left = max(current_mountain['left'], previous_mountain['left'])
            leftmost_right = min(current_mountain['right'], previous_mountain['right'])
            intersection_base = leftmost_right - rightmost_left
            if(intersection_base > 0):
                intersection_height = 0.5 * intersection_base
                intersection_area = 0.5 * intersection_base * intersection_height
                
                current_mountain_area -= intersection_area
            
        visible_area += current_mountain_area
    return visible_area
            



def main():
    mountains = [
        {'left': 9, 'right': 15, 'height': 3},
        {'left': 8, 'right': 14, 'height': 3},
        {'left': 0, 'right':  6, 'height': 3},
    ]

    
    result = visible_area(mountains)
    print("Visible Area:", result)

if __name__ == "__main__":
    main()