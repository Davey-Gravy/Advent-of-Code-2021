# Part 1
# parse input file, split into list
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

# Part 2
# reinitialize pos, initialize aim
pos = [0, 0]
aim = 0
for i in data:
    if i[0] == 'forward':
        pos[0] += int(i[1])
        # implement aim mechanic
        pos[1] += int(i[1])*aim
    elif i[0] == 'down':
        aim += int(i[1])
    else:
        aim -= int(i[1])

print(pos[0]*pos[1])
