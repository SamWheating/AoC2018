import string

# Set this to use the sample input and conditions
DEBUG = False

if DEBUG:
    with open('day7_sample.txt') as f:
        input = f.readlines()
else:
    with open('day7.txt') as f:
        input = f.readlines()

rules = []
for row in input:
    rules.append((row.split(" ")[1], row.split(" ")[7]))

to_do = [letter for letter in string.ascii_uppercase] if not DEBUG else [letter for letter in "ABCDEF"]

p1 = ""
while True:
    blockers = {letter: [] for letter in to_do}
    for rule in rules:
        if rule[1] in blockers.keys() and rule[0] in to_do:
            blockers[rule[1]].append(rule[0])

    available = []
    for letter in blockers.keys():
        if len(blockers[letter]) == 0:
            available.append(letter)

    available = sorted(available, reverse=True)
    letter = available.pop()
    to_do.remove(letter)
    p1 += letter
    if len(to_do) == 0:
        break

print("Part 1: ", p1)

# Part 2:

if DEBUG:
    def task_duration(task):
        # Converts capital letters to numeric indices
        return ord(task) - 64
else:
    def task_duration(task):
        # Converts capital letters to numeric indices + 60
        return ord(task) - 4 

def available_worker(workers):
    # Returns the index of an available worker or False if there aren't any.
    for worker in workers.keys():
        if workers[worker] is None:
            return worker
    return False

def count_available(workers):
    count = 0
    for worker in workers.keys():
        if workers[worker] == None:
            count += 1
    return count

# Track progress in the to_do list
to_do = 'ABCDEF' if DEBUG else string.ascii_uppercase
tasks = {letter: {"remaining": task_duration(letter), "in_progress": False} for letter in to_do}
# Track workers and assignments here:
NUM_WORKERS = 2 if DEBUG else 5
workers = {i+1: None for i in range(NUM_WORKERS)}
p2 = 0
while True:

    blockers = {letter: [] for letter in to_do}
    for rule in rules:
        if rule[1] in blockers.keys() and rule[0] in to_do:
            blockers[rule[1]].append(rule[0])

    available = []
    for letter in blockers.keys():
        if len(blockers[letter]) == 0:
            if not tasks[letter]["in_progress"]:
                available.append(letter)        

    available = sorted(available, reverse=True)

    while len(available) > 0 and available_worker(workers):
        letter = available.pop()
        print("time = ", p2 ,"assigning task ", letter, " to worker #", available_worker(workers))
        workers[available_worker(workers)] = letter
        tasks[letter]["in_progress"] = True

    # update status of all tasks:
    for worker in workers.keys():
        if workers[worker] is not None:
            tasks[workers[worker]]["remaining"] -= 1
            if tasks[workers[worker]]["remaining"] == 0:
                to_do = to_do.replace(workers[worker], "")
                workers[worker] = None

    p2 += 1
    if len(to_do) == 0:
        break

print("Part 2: ", p2)
