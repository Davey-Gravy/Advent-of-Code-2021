# Part 1
# open input file, split separate lines into a list
file = open('day1.dat')
data = [int(i) for i in file.read().splitlines()]

# initialize counter variable
count = 0
# loop through list
for i in range(len(data)-1):
    # check if next value is greater than current value
    if int(data[i]) < int(data[i+1]):
        count += 1

print(count)

# Part 2
# initialize counter
count = 0
window = 3
for i in range(len(data)-3):
    current_sum = sum(data[i:i+3])
    next_sum = sum(data[i+1:i+1+3])
    if next_sum > current_sum:
        count += 1
print(count)
