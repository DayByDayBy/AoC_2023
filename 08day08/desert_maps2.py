import math

def guide():
    map_data = [x for x in open('map.txt').read().strip().split('\n\n')]
    directions  = list(map_data[0])
    nodes = {}
    
    for map in map_data[1].split("\n"):
        a = map.split(" ")[0]
        b = map.split("(")[1].split(",")[0]
        c = map.split(" ")[3].split(")")[0]
        nodes[a] = (b, c)   
         
    key = 'AAA'
    node_count = 0
    while key != 'ZZZ':
        d = directions[node_count % len(directions)]
        key = nodes[key][0 if d == 'L' else 1]
        node_count += 1
    print("node count:", node_count)
    
    def second_half(node):
        key = node
        node_count = 0
        while not key.endswith('Z'):
            d = directions[node_count % len(directions)]
            key = nodes[key][0 if d == 'L' else 1]
            node_count += 1
        return node_count
    end_counter = 1
    for node in nodes:
        if node.endswith('A'):
            end_counter = math.lcm(end_counter, second_half(node))
    print("node counter: ", end_counter)

guide()