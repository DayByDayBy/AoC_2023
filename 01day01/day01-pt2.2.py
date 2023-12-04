import re

def digit_finder():
    
    written_num = {
    'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }
    written_num_rev = {
        'eno': '1', 
        'owt': '2', 
        'eerht': '3', 
        'ruof': '4', 
        'evif': '5', 
        'xis': '6', 
        'neves': '7', 
        'thgie': '8', 
        'enin': '9'
    }
    
    coordinates = []
     
    with open('day01input.txt', 'r') as data:
        for line in data:
            forward = re.finditer('\d|one|two|three|four|five|six|seven|eight|nine', line)
            reverse = re.finditer('\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])
            first_match = next(forward, None)
            last_match = next(reverse, None) 
            first_digit = first_match.group() if first_match else None
            last_digit = last_match.group()[::-1] if last_match else None 
            if first_digit is not None and last_digit is not None:
                a = written_num.get(first_digit, first_digit)
                b = written_num_rev.get(last_digit[::-1], last_digit[::-1])
                coordinate = int(a + b)
                coordinates.append(coordinate)
    return coordinates
print(digit_finder())
print(sum(digit_finder()))