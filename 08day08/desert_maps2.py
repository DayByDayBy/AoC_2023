import math

def guide(file_path):   
    with open(file_path) as data:
        node_dict = {}
        lines = data.read().splitlines()     
    directions = list(lines[0].strip())
    starting_nodes = [key for key in node_dict if key.endswith('A')]  
    
    total = 0
    lcm_steps = 1  
    
    for start_pos in starting_nodes:
        current_node = nodes[start_pos]
        node_count = 0
        
        while current_node != node_dict['ZZZ']:
            for d in directions:
                current_node_key = current_node[0] if d == 'L' else current_node[1] 
                current_node = node_dict[current_node_key]
                node_count += 1
        print(f"steps:{node_count}")  
        total += node_count
        lcm_steps += math.lcm(lcm_steps, node_count)
    print("total: ", total)         
    print("lcm: ", lcm_steps)
         
guide('map.txt')