with open('day1.txt') as f:
    input = f.readlines()
    input = [x.strip('\n') for x in input] 

# Part 1:
total = 0 
for i in range(len(input)):
    num = int(input[i][1:])
    if input[i][0] == '+':
        total += num
    if input[i][0] == '-':
        total -= num

print("Part 1 answer: {}".format(total))

# Part 2:
# Test override input for part 2 (Solution should be 14)
# input= ['+7', '+7', '-2', '-7', '-4']

visited = []
current = 0
i = 0

while True:

    num = int(input[i][1:])
    if input[i][0] == '+':
        current += num
    if input[i][0] == '-':
        current -= num
    i += 1
    if i == len(input):
        i = 0
    if current in visited:
        break
    else:
        visited.append(current)

print("Part 2 answer: {}".format(current))
