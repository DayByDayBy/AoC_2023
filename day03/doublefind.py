import re

def finddouble():
    with open('parts.txt', 'r') as data:
        string = data.read()
        numbers = [int(match) for match in re.findall(r'\d+', string)]
    return numbers
    

print(len(finddouble()))
print(len(set(finddouble())))
print(sum(finddouble()))
print(sum(set(finddouble())))
