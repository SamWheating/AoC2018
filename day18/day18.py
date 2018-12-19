import itertools

with open('day18.txt') as f:
    input = f.readlines()

yard = [list(line.strip("\n")) for line in input]

def get_surrounding(yard, x, y):
    surrounding = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i >=0 and i < len(yard[0])) and (j>=0 and j<len(yard)) and not (i==x and j==y):
                surrounding.append(yard[j][i])
    return surrounding

def process_yard(yard):
    next_yard = [row[:] for row in yard]
    for y in range(len(yard)):
        for x in range(len(yard[0])):
            surrounding = get_surrounding(yard, x, y)

            if yard[y][x] == "." and surrounding.count("|") >= 3:
                next_yard[y][x] = "|"

            if yard[y][x] == "|" and surrounding.count("#") >= 3:
                next_yard[y][x] = "#"

            if yard[y][x] == "#" and surrounding.count("#") >= 1 and surrounding.count("|") >= 1:
                next_yard[y][x] = "#"

            elif yard[y][x] == "#":
                next_yard[y][x] = "."

    return next_yard

# By observation the system converges to a stable cycle of period 28.
# Assume convergence after 1000 iterations
part_2_target = 1000000000
part_2_target = 500 + ((part_2_target - 500) % 28) 

for i in range(part_2_target):

    if i == 10:
        flat_yard = list(itertools.chain.from_iterable(yard))
        print("Part 1: ", flat_yard.count('#') * flat_yard.count("|"))

    yard = process_yard(yard)

flat_yard = list(itertools.chain.from_iterable(yard))
print("Part 2: ", flat_yard.count('#') * flat_yard.count("|"))
