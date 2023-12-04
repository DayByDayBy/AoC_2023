import re

def is_symbol(char):
    return re.search(r'[^0-9.]', char) is not None  # Check if the result is not None to return a boolean

def is_adjacent(number_coords, symbol_locations):
    for x_num_co, y_num_co in number_coords:
        for symbol_x, symbol_y in symbol_locations:
            if abs(symbol_x - x_num_co) <= 1 and abs(symbol_y - y_num_co) <= 1:
                return True
    return False

def partlist():
    numbers = re.compile(r'\d+')
    with open('parts.txt', 'r') as data:
        symbol_locations = []
        adjacent_locations = []
        grid = [list(line.strip()) for line in data]

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if is_symbol(char):
                print(f"Found symbol {char} at ({x}, {y})")
                symbol_locations.append((x, y))  # Use a tuple for symbol locations

    for y, line in enumerate(grid):
        for match in numbers.finditer(''.join(line)):
            start, end = match.span()
            number = match.group()
            x_start, x_end = start, end - 1         
            number_coords = [(x, y) for x in range(x_start, x_end + 1)]

            if is_adjacent(number_coords, symbol_locations):
                adjacent_locations.append(int(number))
                print(number)

    return adjacent_locations

parts = partlist()
print(f"--{len(parts)}")
print(sum(parts))
print(list(parts))
print(sum(list(parts)))
