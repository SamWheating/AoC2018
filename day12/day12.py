SAMPLE = False

stretch = 10000

if SAMPLE:
    with open('day12_sample.txt') as f:
        input = f.readlines()

else:    
    with open('day12.txt') as f:
        input = f.readlines()

if SAMPLE:
    initial = "#..#.#..##......###...###"
else: 
    initial = "##.##.##..#..#.#.#.#...#...#####.###...#####.##..#####.#..#.##..#..#.#...#...##.##...#.##......####."

rules = input
plant_rules = []
for rule in rules:
    if rule[-2] == "#":
        plant_rules.append(rule[:5])

# Part 1:

plants = {i: "." for i in range(-stretch, len(initial) + stretch)}
for i in range(len(initial)):
    if initial[i] == "#":
        plants[i] = "#"

for i in range(20):
    next_plants = {i: "." for i in range(-stretch, len(initial) + stretch)}
    for i in list(plants.keys())[2:-2]:
        aoi = plants[i-2] + plants[i-1] + plants[i] + plants[i+1] + plants[i+2]
        if aoi in plant_rules:
            next_plants[i] = "#" 

    plants = next_plants
    #print("".join([item for item in plants.values()]))
        
count = 0
for i in plants.keys():
    if plants[i] == "#":
        count += i

print("Part 1: {}".format(count))

# Part 2:
# System was observed to hit a quasi-steady state with a consistent +62 plants / generation at some point.

prev_count = 0
plants = {i: "." for i in range(-stretch, len(initial) + stretch)}
for i in range(len(initial)):
    if initial[i] == "#":
        plants[i] = "#"

for age in range(5000):
    next_plants = {i: "." for i in range(-stretch, len(initial) + stretch)}
    for i in list(plants.keys())[2:-2]:
        aoi = plants[i-2] + plants[i-1] + plants[i] + plants[i+1] + plants[i+2]
        if aoi in plant_rules:
            next_plants[i] = "#" 

    plants = next_plants
        
    count = 0
    for i in plants.keys():
        if plants[i] == "#":
            count += i

    if count - prev_count == 62:
        remaining_ages = 50000000000 - (age + 1)
        print("Part 2: {}".format(count+remaining_ages*62))
        break
    prev_count = count