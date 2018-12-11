fuel_cells = [[0 for i in range(300)] for i in range(300)]

serial_number = 9424

for i in range(300):
    for j in range(300):
        rack_id  = i + 11
        power_level = rack_id * (j+1)
        power_level += serial_number
        power_level *= rack_id
        as_string = str(power_level)
        fuel_cells[i][j] = int(as_string[-3]) - 5 

# Part 1:

max_power = 0
for i in range(297):
    for j in range(297):
        sum_power = 0
        sum_power = sum([sum(row[i:i+3]) for row in fuel_cells[j:j+3]])
        if sum_power > max_power:
            max_power = sum_power
            best = [j+1, i+1]

print("Part 1: {}, {}".format(*best))

# Part 2:

max_power = 0
for i in range(300):
    for j in range(300):
        sum_power = 0
        max_size = min([300-i, 300-j])
        for size in range(max_size):
            sum_power = sum([sum(row[i:i+size]) for row in fuel_cells[j:j+size]])
            if sum_power > max_power:
                max_power = sum_power
                best = [j+1, i+1, size]

print("Part 2: {}, {}, {}".format(*best))