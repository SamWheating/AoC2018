import string

with open('day2.txt') as f:
    input = f.readlines()
    input = [x.strip('\n') for x in input] 

# Part 1:

threes = 0
twos = 0
for row in input:
    found_two = False
    found_three = False
    for letter in string.ascii_lowercase:
        if row.count(letter) == 2 and not found_two:
            twos += 1
            found_two = True
        if row.count(letter) == 3 and not found_three:
            threes += 1
            found_three = True

print("part 1:", twos * threes)

# Part 2
outputs = []
for row in input:
    for row2 in input:
        different = 0
        for i in range(len(row)):
            if row[i] != row2[i]:
                different += 1
        if different == 1:
            outputs = [row,row2]
            break
    if different == 1:
        break

output = ""
for i in range(len(row)):
    if outputs[0][i] == outputs[1][i]:
        output += outputs[0][i]

print("part 2: ", output)


