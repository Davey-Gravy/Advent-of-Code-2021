# open input file, split separate lines into a list
file = open('day1.dat')
data = file.read().splitlines()
# initialize counter variable
count = 0
# loop through list
for i in range(len(data)-1):
    # check if next value is greater than current value
    if int(data[i]) < int(data[i+1]):
        count += 1

print(count)
