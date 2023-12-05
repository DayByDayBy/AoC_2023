seeds = [[1] + [numbers.split() for numbers in line.split()] for line in open(r"smallmanac.txt")]

print(f"{seeds}")