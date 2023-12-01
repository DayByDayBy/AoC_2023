# get input 
# iterate over line/string to find first non alpha, ie first int, a
# iterate to end of line/string, find last non-alpha, ie last int, b
# return new int concatenating int a and int b - ab (even if they are the same digit)
# add to list of two digit ints
# sum list of two digit ints
# return sum
# ?????
# profit!

import re

def find_digits():
    coordinates = []

    with open('day01input.txt', 'r') as provided_text:
        for string in provided_text:
            first_num_ind = None
            last_num_ind = None
            nums = re.finditer('\d', string)
        
            for num in nums:
                if first_num_ind is None:
                    first_num_ind = num.start()    
                last_num_ind = num.start()

            if first_num_ind is not None and last_num_ind is not None:
                first_num = string[first_num_ind]
                last_num = string[last_num_ind]
                coordinate = int(first_num + last_num)
                coordinates.append(coordinate)
    return coordinates

    
resulting_list = find_digits()
print(resulting_list)
print(sum(resulting_list))










# print(srtring[first_num_match.start()]

#         first_num = string[index]



# for i, c in enumerate(s):
#         if c.isdigit():
#             print(c)