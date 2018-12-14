input = 633601

elf1 = 0
elf2 = 1
recipies = [3,7]

# Part 1:
while True:
    sum = int(recipies[elf1]) + int(recipies[elf2])

    if sum < 10:
        recipies.append(sum)
    else:
        recipies.extend([1, sum%10])

    elf1 = (elf1 + 1 + recipies[elf1]) % len(recipies)
    elf2 = (elf2 + 1 + recipies[elf2]) % len(recipies)

    if len(recipies) > input+10:
        good = recipies[input:input+10]
        print("Part 1: {}".format("".join(str(i) for i in good)))
        break

# Part 2:
input = [int(letter) for letter in str(input)]
while True:
    sum = int(recipies[elf1]) + int(recipies[elf2])

    if sum < 10:
        recipies.append(sum)
    else:
        recipies.extend([1, sum%10])

    elf1 = (elf1 + 1 + recipies[elf1]) % len(recipies)
    elf2 = (elf2 + 1 + recipies[elf2]) % len(recipies)

    if recipies[-6:] == input:
        print("Part 2: {}".format(len(recipies)-6))

    if recipies[-7:-1] == input:
        print("Part 2: {}".format(len(recipies)-7))
        break
