
def guide():
    node_dict = {}
    with open('smallmap.txt') as data:
        lines = data.read().strip().split('\n')
        directions = lines[0]
        nodes = lines[2:]
        for node_line in nodes:
            parts = node_line.split('=')
            node_name = parts[0].strip()
            node_values = tuple(part.strip() for part in parts[1].strip('()').split(','))
            node_dict[node_name] = node_values
        print(node_dict)         


    def path_find():
        path = list(directions)
        for p in path:
            
        # print(path)
        
    
    path_find()    
guide()
