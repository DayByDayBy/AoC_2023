import re

def is_gear(char):
    return re.search('\\*', char) 

def is_number(char):
    return re.search('\d+', char)


def gears():
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]
        gear_loc = []
        num_loc = []
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if is_gear(char):
                    # print(f"gear at ({x}, {y})")
                    gear_loc.append((x, y))
                if is_number(char):
                    # print(f"{char} at ({x}, {y})")
                    num_loc.append([char, (x, y)])
                    
                
            
    return gear_loc, num_loc
gear_locations, num_locations = gears()
# print("Gear Locations:", gear_locations)
print("Number Locations:", num_locations)
# print(list(gears()))