# Part 1
from collections import Counter
# parse input file, split into list
file = open('day3.dat')
data = file.read().splitlines()
# initialize strings for binary numbers
gamma = ''
epsilon = ''
# loop through each binary number
# determine the most common value for each bit, append to string
for i in range(len(data[0])):
    gamma += Counter([j[i] for j in data]).most_common()[0][0]
    epsilon += Counter([j[i] for j in data]).most_common()[1][0]

print(int(gamma, 2)*int(epsilon, 2))
