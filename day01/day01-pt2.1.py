
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
            
            if first_num is not None and last_num is not None:
                coordinate = int(first_num + last_num)
                coordinates.append(coordinate)
    return coordinates


resulting_list = find_digits()
print(resulting_list)
print(sum(resulting_list))





# with open('day01input.txt', 'r') as data:
#         for string in data:
#             first_matches = re.finditer('\d|one|two|three|four|five|six|seven|eight|nine', string)
#             first = next(first_matches, None)

#             # Output the result for the original order
#             print("Original Order:")
#             if first:
#                 print("First Match:", first.group())

#         for string in data:
#             # Reverse the string and find matches
#             last_matches = re.finditer('\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', string[::-1])
#             last = next(last_matches, None)

#             # Output the result for the reverse order
#             print("\nReverse Order:")
#             if last_num:
#                 print("Last Match (Reverse):", last_num.group()[::-1])




