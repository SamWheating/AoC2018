import copy

# define all of the opcodes:
def addr(registers, command):
    registers[command[3]] = registers[command[1]] + registers[command[2]]
    return registers

def addi(registers, command):
    registers[command[3]] = registers[command[1]] + command[2]
    return registers

def mulr(registers, command):
    registers[command[3]] = registers[command[1]] * registers[command[2]]
    return registers

def muli(registers, command):
    registers[command[3]] = registers[command[1]] * command[2]
    return registers

def banr(registers, command):
    registers[command[3]] = registers[command[1]] & registers[command[2]]
    return registers

def bani(registers, command):
    registers[command[3]] = registers[command[1]] & command[2]
    return registers

def borr(registers, command):
    registers[command[3]] = registers[command[1]] | registers[command[2]]
    return registers

def bori(registers, command):
    registers[command[3]] = registers[command[1]] | command[2]
    return registers

def setr(registers, command):
    registers[command[3]] = registers[command[1]]
    return registers

def seti(registers, command):
    registers[command[3]] = command[1]
    return registers

def gtir(registers, command):
    if command[1] > registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

def gtri(registers, command):
    if registers[command[1]] > command[2]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

def gtrr(registers, command):
    if registers[command[1]] > registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

def eqir(registers, command):
    if command[1] == registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

def eqri(registers, command):
    if registers[command[1]] == command[2]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

def eqrr(registers, command):
    if registers[command[1]] == registers[command[2]]:
        registers[command[3]] = 1
    else:
        registers[command[3]] = 0
    return registers

# Parse the inputs for part 1 into dicts:
with open('day16_1.txt') as f:
    part1 = f.readlines()

i = 0
examples = []
while True:
    example = {}
    example["before"] = [int(i) for i in part1[i][9:19].split(",")]
    example["input"] = [int(i) for i in part1[i+1].split(" ")]
    example["after"] = [int(i) for i in part1[i+2][9:19].split(",")]
    examples.append(example)
    i += 4
    if i >= len(part1):
        break

# Compute answer for part 1:
opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
part1_answer = 0
opcodes_accumulator = []
for example in examples:
    works = []
    for op in opcodes:
        before = copy.deepcopy(example["before"])
        command = copy.deepcopy(example["input"])
        if op(before, command) == example["after"]: 
            works.append(op)
    if len(works) >= 3:
        part1_answer += 1
    opcodes_accumulator.append({"code": command[0], "candidates": works})

print("Part 1: ", part1_answer)

# Part 2
# Find the correct mapping of opcodes to functions
opcodes_mapping = {}

while len(opcodes_mapping) < 16:
    for item in opcodes_accumulator:
        if len(item["candidates"]) == 1:
            found = item["candidates"][0]
            opcodes_mapping[item["code"]] = found
            for unit in opcodes_accumulator:
                if found in unit["candidates"]:
                    unit["candidates"].remove(found)
            break

# Load inputs
with open('day16_2.txt') as f:
    part2 = [[int(i) for i in line.split(" ")] for line in f.readlines()]

# run program
registers = [0,0,0,0]
for line in part2:
    registers = opcodes_mapping[line[0]](registers, line)

print(registers)
