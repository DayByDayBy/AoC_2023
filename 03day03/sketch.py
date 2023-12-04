import re


def adding_padding(grid):
    grid.insert(0, ['.' for _ in range(len(grid[0]))])
    grid.append(['.' for _ in range(len(grid[0]))])
    
def gears():
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]
        gears = []
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if re.search('\\*', char):
                    # print(f"Found '*' at ({x}, {y})")
                    gears.append((x, y))
    return gears 

def numbers():
    with open('parts.txt', 'r') as data:
        grid = [list(line.strip()) for line in data]
        result_numbers = []
        for y, line in enumerate(grid):
            x = 0
            while x < len(line):
                if line[x].isdigit():
                    number = ''
                    while x < len(line) and line[x].isdigit():
                        number += line[x]
                        x += 1
                    result_numbers.append((int(number), (x - len(number), y)))
                else:
                    x += 1

    return result_numbers

def active_gears():
    adding_padding(grid)
    active_gears = []
    return active_gears

       
print(gears())
print(numbers())