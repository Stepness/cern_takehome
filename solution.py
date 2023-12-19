def mountain_area(mountain) -> float:
    return 0.5 * (mountain['right'] - mountain['left']) * mountain['height']
    

def visible_area(mountains: list) -> float:
    for index, mountain in enumerate(mountains):
        current_mountain_area = mountain_area(mountain)
        
        for previous_mountain in mountains[:index]:
            print(mountain_area(previous_mountain))
            



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