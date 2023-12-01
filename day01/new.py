import re

def digit_finder():
    
    coordinates = []
     
    with open('day01input.txt', 'r') as data:
        for line in data:
            forward = re.finditer('\d|one|two|three|four|five|six|seven|eight|nine', line)
            reversed = re.finditer('\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])
            first = 
            last = reversed.finditer(data)
         
            
            
            
            coordinate = (first + last)
            coordinates.append(coordinate)
        return coordinates
print(digit_finder())
            
