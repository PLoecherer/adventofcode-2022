
print("Day 7")

with open("Day7.txt", "r") as file: 

    data = file.read().splitlines()

    parent_directorys = []
    directory_sizes = {}

    for line in data:
        line = line.split(' ')
        if line[0] == '$':
            if line[1] == 'cd' and line[2] != '..':
                parent_directorys.append(line[2])
                directory_sizes['/'.join(parent_directorys)] = 0 
            elif line[1] == 'cd' and line[2] == '..':
                parent_directorys.pop()
        elif line[0] == 'dir':
            directory_sizes['/'.join(parent_directorys) + '/' + line[1]] = 0 
        else:
            directory_sizes['/'.join(parent_directorys)] += int(line[0]) 
            for i in range(1, len(parent_directorys)):
                directory_sizes['/'.join(parent_directorys[:-i])] += int(line[0])

    small_dirs = [value for value in directory_sizes.values() if value <= 100000]
    print("Part 1:", sum(small_dirs))
    freespace = 70000000 - directory_sizes['/']
    delete = 30000000 - freespace
    delete_dirs = [value for value in directory_sizes.values() if value >= delete]
    deldir = sorted(delete_dirs)
    print("Part 2:", min(deldir))
    print(directory_sizes)
