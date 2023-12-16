import math as m, re # maths is cool, that means math is cool too

grid = list(open('parts.txt'))  # not sure if i prefer this to the shorter regex, but figured i'd try it 
locations = {(y, x): [] for y in range(140) for x in range(140)
                    if grid[y][x] not in '01234566789.'}  

for y, row in enumerate(grid):     # 2.1 is way cleaner than pt1 and pt2l; struggle makes strong
    for number in re.finditer(r'\d+', row):
        edge = {(y, x) for y in (y-1, y, y+1)
                       for x in range(number.start()-1, number.end()+1)}
        for e in edge & locations.keys():
            locations[e].append(int(number.group()))
print(sum(sum(p)    for p in locations.values()),
      sum(m.prod(p) for p in locations.values() if len(p)==2))