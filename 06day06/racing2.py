import numpy as np

def acceleration_movement_pairs(n):
    pairs = []
    for i in range(1, n):
        pairs.append((i, n - i))
    return pairs

def boatracer():
    race_data = open('races.txt').read()
    times, distances = race_data.split('\n')[:2]
    time = int(''.join(times.split(':')[1].strip().split()))
    distance = int(''.join(distances.split(':')[1].strip().split()))
    # print(time, distance)
    attempt_list = []
    possible_attempts = 0
        
    for i in acceleration_movement_pairs(time):
        if i[0]*i[1] > distance:
            possible_attempts += 1
    attempt_list.append(possible_attempts)                      
    return np.prod(attempt_list)
    
print(boatracer())