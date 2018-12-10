with open('day4.txt') as f:
    input = f.readlines()
    input = [x.strip('\n') for x in input] 

# parsers:
def get_date(row):
    return int(row[6:8] + row[9:11])

def get_time(row):
    time = int(row[12:14] + row[15:17])
    return time

def get_guard(row):
    return int(row[row.index("#")+1:].split(" ")[0])

days = []
guards = []
for row in input:
    days.append(get_date(row))
    if "#" in row:
        guards.append(get_guard(row))

# Tmiestamp and sort all records

timestamped_records = []

for row in input:
    date = int(row[6:8] + row[9:11])
    time = int(row[12:14] + row[15:17])
    ts = (date * 10000 + time)
    timestamped_records.append((ts, row))

timestamped_records = sorted(timestamped_records, key=lambda tup: tup[0])

for record in timestamped_records:
    print(record)

# Count minutes slept per guard
sleeping_minutes = {guard: 0 for guard in guards}

active_guard = 0 
asleep = False
time_asleep = 0
nap_length = 0
for record in timestamped_records:
    row = record[1]
    if row[-5:] == "shift":
        active_guard = get_guard(row)
    elif row[-6:] == "asleep":
        asleep = True
        time_asleep = get_time(row)
    elif row[-2:] == "up":
        asleep = False
        time_awake = get_time(row)
        sleeping_minutes[active_guard] += (time_awake - time_asleep)

sleepiest = 0
most_sleep = 0
for guard in guards:
    if sleeping_minutes[guard] > most_sleep:
        sleepiest = guard
        most_sleep = sleeping_minutes[guard]

print("sleepiest guard: #", sleepiest, " slept ", most_sleep, " minutes.")

# Count how many times the sleepiest guard slept each minute
asleep = False
minute_asleep = 0
minute_awake = 0
sleep_record = {i : 0 for i in range(60)}
for record in timestamped_records:
    row = record[1]
    if row[-5:] == "shift":
        active_guard = get_guard(row)

    if active_guard == sleepiest:
        if row[-6:] == "asleep":
            asleep = True
            minute_asleep = get_time(row)
        elif row[-2:] == "up":
            asleep = False
            minute_awake = get_time(row)
            for i in range(minute_asleep, minute_awake):
                sleep_record[i] += 1

sleepiest_minute = 0
most_sleep = 0
for i in range(60):
    if sleep_record[i] > most_sleep:
        sleepiest_minute = i
        most_sleep = sleep_record[i]

print("sleepiest minute: ", sleepiest_minute)
print("Part 1: ", sleepiest_minute*sleepiest)

# part two: which guard sleeps the most in a single minute?

asleep = False
minute_asleep = 0
minute_awake = 0
sleep_record = {guard: {i : 0 for i in range(60)} for guard in guards}
for record in timestamped_records:
    row = record[1]
    if row[-5:] == "shift":
        active_guard = get_guard(row)
    if row[-6:] == "asleep":
        asleep = True
        minute_asleep = get_time(row)
    elif row[-2:] == "up":
        asleep = False
        minute_awake = get_time(row)
        print(active_guard, " slept from ", minute_asleep, " until ", minute_awake)
        for i in range(minute_asleep, minute_awake):
            sleep_record[active_guard][i] += 1

print(sleep_record)

sleepiest_guy = 0
sleepiest_minute = 0
most_sleep = 0
for guard in guards:
    for i in range(60):
        if sleep_record[guard][i] > most_sleep:
            most_sleep = sleep_record[guard][i]
            sleepiest_guy = guard
            sleepiest_minute = i

print("guard ", sleepiest_guy, " slept ", most_sleep, " times during minute ", sleepiest_minute)



print("Part 2: ", sleepiest_guy*sleepiest_minute)


