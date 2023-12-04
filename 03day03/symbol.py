import re

def is_symbol(char):
    return re.search(r'[^0-9.]', char)
        
def symbols():
    with open('parts.txt', 'r') as data:
            symbol_locations = []
            grid = [list(line.strip()) for line in data]
            for y, line in enumerate(grid):
                for x, char in enumerate(line):
                    if is_symbol(char):
                        print(f"Found symbol {char} at ({x}, {y})")
                        symbol_locations.append((char, [x, y]))
            return symbol_locations
    
            
print(symbols())
        