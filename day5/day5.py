import string

with open('day5.txt') as f:
    input = f.readlines()
    original_input = input[0].strip('\n')

# override input for testing
# original_input = "dabAcCaCBAcCcaDA"

input = original_input
while(True):
    matched = False
    i  = 0
    while(True):
        if input[i].lower() == input[i+1].lower() and input[i] != input[i+1]:
            matched = True
            input = input[:i] + input[i+2:]

        i += 1
        if i >= len(input)-2: 
            break

    if not matched:
        print("Part 1: ", len(input))
        break

pairs_length = {letter: 0 for letter in string.ascii_lowercase}

for letter in string.ascii_lowercase:

    input = original_input.replace(letter.upper(), "").replace(letter, "")

    while(True):
        matched = False
        i  = 0
        while(True):
            if input[i].lower() == input[i+1].lower() and input[i] != input[i+1]:
                matched = True
                input = input[:i] + input[i+2:]

            i += 1
            if i >= len(input)-2: break

        if not matched:
            pairs_length[letter] = len(input)
            break

print("Part 2: ", min(pairs_length.values()))
