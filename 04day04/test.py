tickets = [[line[0].split()[-1]]+[nums.split() for nums in line[9:].split(" | ")] for line in open( r"small.txt")]

# not quite, gives a int/str error
# that's what i get for trying to be clever 
# still, gonna leave it here to remind me