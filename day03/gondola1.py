import re

def is_adjacent(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

def partlist():
    symbol_locations = []
    number_locations = []
    adjacent_locations = set()

    symbols = re.compile(r'[^0-9a-zA-Z.]')
    numbers = re.compile(r'\d+')
    
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if symbols.search(char):
                symbol_locations.append((x, y))

    for y, line in enumerate(grid):
        for match in numbers.finditer(''.join(line)):
            start, end = match.span()
            number = match.group()
            x_start, x_end = start, end - 1         
            number_coords = [(x, y) for x in range(x_start, x_end + 1)]
            for x_num_co, y_num_co in number_coords:
                if any(is_adjacent(x_num_co, y_num_co, symbol_x, symbol_y) for symbol_x, symbol_y in symbol_locations):
                    adjacent_locations.add(int(number))
                    print(f"Added adjacent number: {number}")

    return list(adjacent_locations)

parts = partlist()
print(sum(parts))
