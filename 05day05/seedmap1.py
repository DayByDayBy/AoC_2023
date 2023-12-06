# seeds = [[numbers.split() for numbers in line.split(': ')] for line in open(r"smallmanac.txt")]
# print(seeds)
# seeds = [[int(num) for num in line.split()] for line in open("smallmanac.txt")]

# print(f"{seeds}")

def process_data(file_path):

    data_dict = {}
    seeds = []
    current_section = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('seeds:'):
                seeds = line.split()[1:]
                print(seeds)
            if line.endswith('map:'):
                current_section = line.replace(' map:', '')
                data_dict[current_section] = []
            elif current_section is not None:
                data_list = list(map(int, line.split()))
                data_dict[current_section].append(data_list)
    for key, value in data_dict.items():
        print(f"{key}: {value}")
        
        
        
#         
#   seed = seed
#   s = soil
#   f = fertilizer
#   w = water
#   l = light
#   t = temperature
#   h = humidity
#   l = location
#   
# 

#   
# 
#         
#         
#         
#   
#   
# 
#         
#         


process_data('smallmanac.txt')
