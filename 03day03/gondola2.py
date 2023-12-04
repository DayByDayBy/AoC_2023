import re

def is_gear(char):
    return re.search('\\*', char) 

def is_number(line):
    return re.findall('\d+',  ''.join(line))
         

def is_active_gear(gear_loc, num_loc):
    for g_x, g_y in gear_loc:
        for number, (n_x, n_y) in num_loc:
            if abs(g_x - n_x) <= 1 and abs(g_y - n_y) <= 1:
                return True
    return False

def gears():
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]
        gear_loc = []
        num_loc = []
        engaged_gears = []
  
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if is_gear(char):
                    print(f"gear at ({x}, {y})")
                    gear_loc.append((x, y))
                numbers = is_number(line)
                for number in numbers:
                    print(f"{char} at ({x}, {y})")
                    num_loc.append([number, (x, y)]) 
                    if is_active_gear(num_loc, gear_loc):                   
                        engaged_gears.append(int(number))                                                                                                    
    return gear_loc, num_loc, engaged_gears


gear_locations, num_locations, engaaged_gears = gears()
# print("Gear Locations:", gear_locations)
# print(num_locations)
print("Number Locations:", num_locations)
# print(list(gears()))