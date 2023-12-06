# seeds = [[numbers.split() for numbers in line.split(': ')] for line in open(r"smallmanac.txt")]
# print(seeds)
# seeds = [[int(num) for num in line.split()] for line in open("smallmanac.txt")]

# print(f"{seeds}")

def capture(file_path):

    almanac = {}
    seeds = []
    current_section = None
    with open(file_path, 'r') as file:
        
        for line in file: # this is now working, grabs the data and makes it nice 
            line = line.strip()
            if line.startswith('seeds:'):
                seeds = line.split()[1:]
                print(seeds)
            if line.endswith('map:'):
                current_section = line.replace(' map:', '')
                almanac[current_section] = []
            elif current_section is not None and line:
                data_list = list(map(int, line.split()))
                almanac[current_section].append(data_list)
                
    for key, value in almanac.items():
        print(f"{key}: {value}")
        
    for key, value in almanac.items():
        for key in almanac:
            for i in value:  
                seed = i[0]
                soil = i[1]
                shift = i[2]
                print()
            
        
    # for i in almanac:
    #     print(value[i][0])
   
    print(almanac)
    
    # for i in seeds():
        
        
        
        
    

        
    
    
    print(seeds)
        
        
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
# seed to soil > soil to fertilizer > fertilizer to water
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


capture('smallmanac.txt')
