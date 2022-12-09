from turtle import position
import numpy as np
import copy
print("Day 9")

def move_tail(head, tail):
    distance = head - tail
    if abs(distance[0]) == 2:
        tail += np.sign(distance)
    if abs(distance[1]) == 2:
        tail += np.sign(distance)
    return tail

with open("Day9.txt", "r") as file: 
    data = file.read()
    commands = data.splitlines()
    for line in range(len(commands)):
        commands[line] = commands[line].split()
        commands[line][1] = int(commands[line][1])
    
    command_to_move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    positions = np.zeros((10,2)) #0: H, 1: T ... 9: Tail 9
    visited = set()
    visited_tail9 = set()

    for line in commands:
        steps = line[1]
        for _ in range(steps):
            positions[0] += command_to_move[line[0]]
            for tail in range(1, len(positions)):
                positions[tail] = move_tail(positions[tail - 1], positions[tail])
            
            visited.add(str(positions[1]))
            visited_tail9.add(str(positions[9]))

    print("Part 1: the tail visited", len(visited), "spaces\n","Part 2: tail 9 visited", len(visited_tail9), "spaces")
