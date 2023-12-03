import re

data_string = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def matcher(number_locations, symbol_locations):
 
    for _, num_coords in number_locations:
        for x_num_co, y_num_co in num_coords:
            for symbol_x, symbol_y in symbol_locations:
                if (
                    abs(symbol_x - x_num_co) <= 1 and abs(symbol_y - y_num_co) <= 1
                ):
                    return True
    return False



def partlist():
    symbol_locations = []
    number_locations = []
    adjacent_locations = []
    symbols = re.compile(r'[^0-9a-zA-Z.]')
    numbers = re.compile(r'\d+')
    
    # with open('dummyparts.txt', 'r') as data:
    grid = [list(line.strip()) for line in data_string.split('\n')]
        
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if symbols.search(char):
                symbol_locations.append((x, y))
    
    for y, line in enumerate(grid):
        for match in numbers.finditer(''.join(line)):
            start, end = match.span()
            number = match.group()
            x_start, x_end = start, end - 1         
            number_locations.append((number, [(x, y) for x in range(x_start, x_end + 1)]))
            
            if matcher(number_locations, symbol_locations):
                adjacent_locations.append(int(number))
                print(f"Added adjacent number: {number}")

    return adjacent_locations

parts = partlist()
# partnumbers = parts
# print(len(parts))
print(sum(parts))


# print(467+114+35+633+617+58+592+755+664+598)

467+35+633+617+592+755+664+598

