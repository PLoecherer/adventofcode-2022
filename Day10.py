import numpy as np
print("Day 10")

with open("Day10.txt", "r") as file: 
    data = file.read()
    commands = data.splitlines()
    commands = [line.split() for line in commands]
    x_cycle = [1, 0]
    cycles = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

    for line in commands:
        if line[0] == 'addx':
            x_cycle[1] += 1
            if x_cycle[1] in cycles:
                cycles[x_cycle[1]] = x_cycle[0]
            x_cycle[1] += 1
            if x_cycle[1] in cycles:
                cycles[x_cycle[1]] = x_cycle[0]
            x_cycle[0] += int(line[1])
        elif line[0] == 'noop':
            x_cycle[1] += 1
            if x_cycle[1] in cycles:
                cycles[x_cycle[1]] = x_cycle[0]

    signalstrengths = [20, 60, 100, 140, 180, 220]
    sigstrengthsum = 0
    for signal in signalstrengths:
       sigstrengthsum += cycles[signal] * signal
    print("Part 1: Sum of Signal Strength at critical values:" , sigstrengthsum)

    #Part 2:
    x_cycle = [1, 0]
    CRT = [['.' for y in range(40)] for x in range(6)]
    row = 0

    for line in commands:
        if line[0] == 'addx':
            if x_cycle[1] == 40:
                row += 1
                x_cycle[1] = 0
            if x_cycle[1] == x_cycle[0] or x_cycle[1] == x_cycle[0] -1 or x_cycle[1] == x_cycle[0] +1:
                CRT[row][x_cycle[1]] = '#'
            x_cycle[1] += 1
            if x_cycle[1] == 40:
                row += 1
                x_cycle[1] = 0
            if x_cycle[1] == x_cycle[0] or x_cycle[1] == x_cycle[0] -1 or x_cycle[1] == x_cycle[0] +1:
                CRT[row][x_cycle[1]] = '#'
            x_cycle[1] += 1
            x_cycle[0] += int(line[1])
        elif line[0] == 'noop':
            if x_cycle[1] == 40:
                row += 1
                x_cycle[1] = 0
            if x_cycle[1] == x_cycle[0] or x_cycle[1] == x_cycle[0] -1 or x_cycle[1] == x_cycle[0] +1:
                CRT[row][x_cycle[1]] = '#'
            x_cycle[1] += 1
            
    print("Part 2:\n")
    for line in CRT:
        print(*line)
