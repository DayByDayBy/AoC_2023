
from functools import reduce

def seedmap(data_link):
    data = open(data_link).read()
    seed_list, *mappings = data.split('\n\n')
    seeds = list(map(int, seed_list.split()[1:]))
    # all_seeds = [num for start, end in zip(seeds[::1], seeds[1::2]) for num in range(start, end + 1)]
    # all_seeds = []
    # for i in range(0, len(seeds), 2):
    #     seed_start = seeds[i]
    #     seed_range = seeds[i+1]
    #     spread = range(seed_start, seed_start+seed_range)     
    #     all_seeds.extend(spread)
    # print(all_seeds)
    
    
    all_seeds_gen = (value for i in range(0, len(seeds), 2) for value in range(seeds[i], seeds[i] + seeds[i+1]))

        
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

    final_locations = [reduce(findmin, mappings, seed) for seed in all_seeds_gen]
    min_result = min(final_locations)

    print(f"minimum: {min_result}")

# seedmap('smallmanac.txt')
seedmap('almanac.txt')