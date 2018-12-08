import string
import math

with open('day6.txt') as f:
    input = f.readlines()

def count_closest(points, size):
    """ Count all of the points which are definitively closest to a certain point """
    coordinates = []
    for row in points:
        x = int(row.split(",")[0]) + int(0.5*size)
        y = int(row.split(",")[1]) + int(0.5*size)
        coordinates.append((x,y))

    area = [[1000 for i in range(size)] for i in range(size)]

    def closest(point, coordinates):
        min = size*10
        best = 1000
        tied = True
        for i in range(len(coordinates)):
            distance = math.fabs(coordinates[i][0] - point[0]) + math.fabs(coordinates[i][1] - point[1])
            if distance < min:
                min = distance
                best = i
                tied = False
            elif distance == min:
                tied = True
        if tied:
            return 1000
        return best

    for i in range(size):
        for j in range(size):
            coordinate = (i, j)
            area[i][j] = closest(coordinate, coordinates)

    tallies = {}
    for j in range(size):
        for k in range(size):
            try:
                tallies[str(area[j][k])] += 1
            except KeyError:
                tallies[str(area[j][k])] = 1

    return tallies

# Part 1:
experiment_size = 800
big = count_closest(input, experiment_size)
bigger = count_closest(input, experiment_size + 2)

largest = 0
for type in big.keys():
    if big[type] == bigger[type]:
        if big[type] > largest:
            largest, max_class = big[type], type

print("Part 1: ", largest, " class: ", type)

# Part 2:

coordinates = []
for row in input:
    x = int(row.split(",")[0])
    y = int(row.split(",")[1])
    coordinates.append((x,y))

zone = 10000
sweep_x_negative = min([c[0] for c in coordinates])
sweep_x_positive = max([c[0] for c in coordinates])
sweep_y_negative = min([c[1] for c in coordinates])
sweep_y_positive = max([c[1] for c in coordinates])
count = 0

for i in range(sweep_x_negative, sweep_x_positive):
    for j in range(sweep_y_negative, sweep_y_positive):
        sum_distance = 0
        for coord in coordinates:
            sum_distance += (math.fabs(i - coord[0]) + math.fabs(j - coord[1]))
            if sum_distance >= zone:
                break
        if sum_distance < zone:
            count += 1
        
print("Part 2: ", count)