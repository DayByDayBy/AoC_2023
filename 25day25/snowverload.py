with open('wiring_diagram.txt') as wiring:
    lines = wiring.readlines()
    for line in lines:
        print(line)  