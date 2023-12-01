
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
    with open('day01input.txt', 'r') as provided_text:
        for string in provided_text:
            first_num = None
            last_num = None
            nums = re.finditer('\d|one|two|three|four|five|six|seven|eight|nine', string)
        
            for num in nums:
                match = num.group()
                if match.isdigit():
                    last_num = match
                    if first_num is None:
                        first_num = last_num
                else:
                    last_num = written_num.get(match, 0)
                    if first_num is None:
                        first_num = last_num

            if first_num is not None and last_num is not None:
                coordinate = int(first_num + last_num)
                coordinates.append(coordinate)
    return coordinates

resulting_list = find_digits()
print(resulting_list)
print(sum(resulting_list))