import re

def is_symbol(char):  # checking whether symbol, ie 'not numeric or period''
    return re.search(r'[^0-9.]', char) is not None  

def is_adjacent(number_coords, symbol_locations): # checking whether any digtit is adjacent, incl diagonals
    for x_num_co, y_num_co in number_coords:
        for symbol_x, symbol_y in symbol_locations:
            if abs(symbol_x - x_num_co) <= 1 and abs(symbol_y - y_num_co) <= 1:
                return True
    return False # assumption is not-adjacent, more likely condition

def partlist():
    numbers = re.compile(r'\d+') # regex number finder, 'digits til not digits', or 'one or more digits'
    with open('parts.txt', 'r') as data: # basic opener - 'r' is default, but tbh i didnt know that wheni wrote this, i found out whole coding this
        symbol_locations = []
        adjacent_locations = []
        grid = [list(line.strip()) for line in data] # grid is a list of lists, a 2D array with line modelled as vertical, position as horizontal

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if is_symbol(char):
                print(f"Found symbol {char} at ({x}, {y})")  # verbose prints, handy for late-night coding with too many tabs
                symbol_locations.append((x, y))

    for y, line in enumerate(grid):
        for match in numbers.finditer(''.join(line)):  # numbers, gotta stitch em together
            start, end = match.span() # start and end of number, necesaary for adjacency checking without multi-digit dupes
            number = match.group()
            x_start, x_end = start, end - 1         
            number_coords = [(x, y) for x in range(x_start, x_end + 1)] # adjacency checking the range of the whole number 

            if is_adjacent(number_coords, symbol_locations):
                adjacent_locations.append(int(number))
                print(number)
    return adjacent_locations

# some more of that over-verbose printing

parts = partlist()
print(f"--{len(parts)}")
print(sum(parts))
print(list(parts))
print(sum(list(parts)))
