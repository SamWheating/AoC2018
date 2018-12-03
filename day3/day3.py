with open('day3.txt') as f:
    input = f.readlines()
    input = [x.strip('\n') for x in input] 

CLOTH_SIZE = 1000

#input = ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]

# Part 1: counting areas with >2 overlaps

cloth = [[0 for i in range(CLOTH_SIZE)]for i in range(CLOTH_SIZE)]
claims = []

for line in input:
    claim_id = int(line[1:line.index("@")])
    left_gap = int(line[line.index("@")+1:line.index(",")])
    top_gap = int(line[line.index(",")+1:line.index(":")])
    width = int(line[line.index(":")+1:line.index("x")])
    height = int(line[line.index("x")+1:])
    claims.append(claim_id)

    for i in range(left_gap, left_gap + width):
        for j in range(top_gap, top_gap + height):
            cloth[i][j] += 1

total = 0
for i in range(CLOTH_SIZE):
    for j in range(CLOTH_SIZE):
        if cloth[i][j] >= 2:
            total += 1

print("Part 1 solution: {}".format(total))

# Part 2: finding the claim with no overlap
# This is soooo innefficient.. O(N^3)? but it computes in ~1 minute.

cloth = [[[] for i in range(CLOTH_SIZE)]for i in range(CLOTH_SIZE)]
claims = []

for line in input:
    claim_id = int(line[1:line.index("@")])
    left_gap = int(line[line.index("@")+1:line.index(",")])
    top_gap = int(line[line.index(",")+1:line.index(":")])
    width = int(line[line.index(":")+1:line.index("x")])
    height = int(line[line.index("x")+1:])
    claims.append(claim_id)

    for i in range(left_gap, left_gap + width):
        for j in range(top_gap, top_gap + height):
            cloth[i][j].append(claim_id)

for claim in claims:
    untouched = True
    for i in range(CLOTH_SIZE):
        for j in range(CLOTH_SIZE):
            if claim in cloth[i][j]:
                if len(cloth[i][j]) > 1:
                    untouched = False

            if untouched == False: break
        if untouched == False: break

    if untouched == True:
        print("Part 2 solution: {}".format(claim))
        break