
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
        # print(node_dict)         

# quick sketch


    def path_find():
        path = list(directions)
        node_dest = node_dict['AAA']
        node_count = 0
        for node in node_dict:
            while node_dest is not 'ZZZ':
                for p in path in range(len(path)):
                    if p == 'L':
                        node_dest = node[0]  
                        node_count += 1
                    elif p == 'R':
                        node_dest = node[1]
                        node_count += 1
            else:
                print(node_count)

                            
                
        print(path)
        
    
    path_find()    
guide()


# some not-quote logic, lol - dinner and another look