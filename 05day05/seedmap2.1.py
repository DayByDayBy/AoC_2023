
seeds, *blocks = open('smallmanac.txt').read().split('\n\n')
seeds = list(map(int, seeds.split(':')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
       ranges.append(list(map(int, line.split())))
    new= []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x <b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)
        print(seeds)
                
    seeds = new


