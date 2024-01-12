import numpy as np

def acceleration_movement_pairs(n):
    pairs = []
    for i in range(1, n):
        pairs.append((i, n - i))
    return pairs

def boatracer():
    race_data = open('races.txt').read()
    times, distances = race_data.split('\n')[:2]
    times = [int(num) for num in times.split(':')[1].split()]
    distances = [int(num) for num in distances.split(':')[1].split()]
    records = list(zip(times, distances))
    print(records)
    attempt_list = []

    
    for record in records:
        possible_attempts = 0
        for i in acceleration_movement_pairs(record[0]):
            if i[0]*i[1] > record[1]:
                possible_attempts += 1
        attempt_list.append(possible_attempts)
        
                        
    print(attempt_list)
    return np.prod(attempt_list)
    

    
print(boatracer())