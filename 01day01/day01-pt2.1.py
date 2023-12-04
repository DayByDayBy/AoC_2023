import re

def find_digits():
    coordinates = []
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
    
    with open('day01input.txt', 'r') as data:
        for string in data:
            first_num = re.finditer('\d|one|two|three|four|five|six|seven|eight|nine', string)
            last_num = re.finditer('\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', string[::-1])
            first = next(first_num, None)
            last = next(last_num, None)
                
            if first.group().isdigit() and last.group().isdigit():
                a = first.group()
                b = last.group()[::-1]
            else:
                a = written_num.get(first.group(), '0')
                b = written_num.get(last.group()[::-1], '0')
            coordinate = int(a + b)
            coordinates.append(coordinate)
    return coordinates




resulting_list = find_digits()
print(resulting_list)
print(sum(resulting_list))
