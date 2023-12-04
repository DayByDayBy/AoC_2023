import re

def is_gear(char):
    return re.search('\\*', char) 

def extract_numbers(y, line):
    return [(int(number), (x, y)) for x, number in enumerate(re.findall('\d+', ''.join(line)))]

def find_adjacent_numbers(gear_loc, num_loc):
    adjacent_numbers = []
    for g_x, g_y in gear_loc:
        for number, (n_x, n_y) in num_loc:
            if abs(g_x - n_x) <= 1 and abs(g_y - n_y) <= 1:
                adjacent_numbers.append(number)
    return adjacent_numbers

def process_gears(grid):
    gear_loc = []
    num_loc = []
    product_list = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if is_gear(char):
                gear_loc.append((x, y))
            num_loc.extend(extract_numbers(y, line))

    for g_x, g_y in gear_loc:
        adjacent_numbers = find_adjacent_numbers(gear_loc, num_loc)
        if len(adjacent_numbers) == 2:
            product_list.append(adjacent_numbers[0] * adjacent_numbers[1])

    return gear_loc, num_loc, product_list

def gears():
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]
        return process_gears(grid)

gear_locations, num_locations, product_list = gears()
print("Number Locations:", num_locations)
print("Product List:", product_list)
