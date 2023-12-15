def part1(file):
    seeds, *mappings = open(file).read().split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))
    for mapping in mappings:
        ranges = []
        for line in mapping.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new= []
        for x in seeds:
            for a, b, c in ranges:
                if b <= x <b + c:
                    new.append(x - b + a)
                    break
            else:
                new.append(x)
        seeds = new
    print(f"lowest: {min(seeds)}")
    
part1('smallmanac.txt')
part1('almanac.txt')

def part2(file):
    initial, *mappings = open(file).read().split('\n\n')
    initial = list(map(int, initial.split(':')[1].split()))
    seeds = [] 
    for i in range(0, len(initial), 2):
        seeds.append((initial[i], initial[i] + initial[i + 1]))
    #  print(seeds)
              
    for mapping in mappings:
        ranges = []
        for line in mapping.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new= []
        
        while seeds:
            start, end = seeds.pop()
            for a, b, c in ranges:
                overlap_start = max(start, b) 
                overlap_end = min(end, b + c)
                if overlap_start < overlap_end:
                    new.append((overlap_start - b + a, overlap_end - b + a))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
                        
        seeds = new
    print(f"range-low: {min(seeds)[0]}")
    with open('day05min.txt', 'w') as file:
        file.write(f"range-low: {min(seeds)[0]}")
    
part2('smallmanac.txt')
part2('almanac.txt')

