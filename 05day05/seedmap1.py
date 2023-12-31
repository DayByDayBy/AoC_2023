
from functools import reduce

def seedmap(data_link):
    data = open(data_link).read()
    seeds, *mappings = data.split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    def findmin(start, mapping):
        for m in mapping.split('\n')[1:]:
            destination, source, length = map(int, m.split())
            spread = start - source
            if spread in range(length):
                result = destination + spread
                # print(f"{mapping}, {start}, {result}")
                return result
        else:
            # print(f"{mapping}, {start}, {start}")
            return start

    final_locations = [reduce(findmin, mappings, seed) for seed in seeds]
    min_result = min(final_locations)

    print(f"minimum: {min_result}")

seedmap('smallmanac.txt')
seedmap('almanac.txt')