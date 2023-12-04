import re

def is_gear(char):
    return re.search('\\*', char) 

def is_number(line):
    return re.findall('\d+',  ''.join(line))

def is_active_gear(num_loc, gear_loc):
    engaged_gears = []
    gears = gear_loc
    for gear in gears:
        if num_loc is in gear_loc:
            return True


    for symbol_x, symbol_y in symbol_coordinates:
        for string, (string_x, string_y) in string_locations:
            # Check if the coordinates are adjacent
            if abs(symbol_x - string_x) <= 1 and abs(symbol_y - string_y) <= 1:
                adjacent_numbers.append(int(string))







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
                numbers = is_number(line)
                for number in numbers:
                    # print(f"{char} at ({x}, {y})")
                    num_loc.append([number, (x, y)])                                
    return gear_loc, num_loc


gear_locations, num_locations = gears()
# print("Gear Locations:", gear_locations)
# print(num_locations)
print("Number Locations:", num_locations)
# print(list(gears()))