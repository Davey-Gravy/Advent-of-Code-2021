# Part 1
# parse input file, split into
file = open('day2.dat')
data = [i.split() for i in file.read().splitlines()]

# initialize x and y variables
pos = [0, 0]

# for each command, increment the associated value
for i in data:
    if i[0] == 'forward':
        pos[0] += int(i[1])
    elif i[0] == 'down':
        pos[1] += int(i[1])
    else:
        pos[1] -= int(i[1])

print(pos[0]*pos[1])
