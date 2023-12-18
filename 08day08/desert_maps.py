def guide(file_path):   
    with open(file_path) as data:
        node_dict = {}
        lines = data.read().splitlines()
    directions = list(lines[0].strip())
    for line in lines[1:]:
        parts = line.split('=')
        if len(parts) == 2:
            node_key = parts[0].strip()
            node_values = tuple(part.strip() for part in parts[1].replace('(', '').replace(')', '').split(','))      
            node_dict[node_key] = node_values
                         
    def path_find():
        path = list(directions)
        current_node = node_dict['AAA']
        node_count = 0   
        while current_node != node_dict['ZZZ']:
            for p in path:
                if p == 'L':
                    current_node_key = current_node[0]
                    current_node = node_dict[current_node_key]
                    node_count += 1
                elif p == 'R':
                    current_node_key = current_node[1]
                    current_node = node_dict[current_node_key]
                    node_count += 1
        print(f"steps:{node_count}")              
    path_find()
guide('map.txt')