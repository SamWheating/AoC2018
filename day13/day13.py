from operator import itemgetter

def get_input(filename):

    with open(filename) as f:
        maze = f.readlines()

    # turn input into arrays:
    maze = [[letter for letter in line] for line in maze]

    # Start by removing all cars from the maze and saving their state in a list of cars
    cars = []
    id= 0
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "v":
                cars.append({"row": row, "col":col, "direction":"down", "prev_turn":"right", "id":id})
                maze[row][col] = "|"
                id += 1
            elif maze[row][col] == ">":
                cars.append({"row": row, "col":col, "direction":"right", "prev_turn":"right", "id":id})
                maze[row][col] = "-"
                id += 1
            elif maze[row][col] == "<":
                cars.append({"row": row, "col":col, "direction":"left", "prev_turn":"right", "id":id})
                maze[row][col] = "-"
                id += 1
            elif maze[row][col] == "^":
                cars.append({"row": row, "col":col, "direction":"up", "prev_turn":"right", "id":id})
                maze[row][col] = "|"
                id += 1
    return cars, maze


def turn_right(direction):
    if direction == "right": return "down"
    elif direction == "down": return "left"
    elif direction == "left": return "up"
    elif direction == "up": return "right"

def turn_left(direction):
    if direction == "right": return "up"
    elif direction == "down": return "right"
    elif direction == "left": return "down"
    elif direction == "up": return "left"

def part_1(cars, maze):
    i = 0
    Running = True
    while Running:
        for car in sorted(cars, key=itemgetter("row", "col")):
            y = car["row"]
            x = car["col"]
            # if car["id"] == 5:
            #     print(x, y, car["direction"], "car #", car["id"])
            current_spot = maze[y][x]
            prev_turn = car["prev_turn"]

            # Process turns (if applicable)
            if current_spot == "+":
                if car["prev_turn"] == "right":
                    car["direction"] = turn_left(car["direction"])
                    car["prev_turn"] = "left"
                elif car["prev_turn"] == "left":
                    car["prev_turn"] = "straight"
                elif car["prev_turn"] == "straight":
                    car["prev_turn"] = "right"
                    car["direction"] = turn_right(car["direction"])

            elif current_spot == "/":
                if car["direction"] == "right": car["direction"] = "up"
                elif car["direction"] == "down": car["direction"] = "left"
                elif car["direction"] == "left": car["direction"] = "down"
                elif car["direction"] == "up": car["direction"] = "right"

            elif current_spot == "\\":
                if car["direction"] == "right": car["direction"] = "down"
                elif car["direction"] == "down": car["direction"] = "right"
                elif car["direction"] == "left": car["direction"] = "up"
                elif car["direction"] == "up": car["direction"] = "left"

            # Apply movements:
            if car["direction"] == "right": car["col"] += 1
            elif car["direction"] == "left": car["col"] -= 1
            elif car["direction"] == "down": car["row"] += 1
            elif car["direction"] == "up": car["row"] -= 1

            # Check collisions:
            positions = [(car["row"], car["col"]) for car in cars]
            if len(positions) != len(set(positions)):
                for position in positions:
                    if positions.count(position) > 1:
                        print("Part 1: Collision at {},{}".format(position[1], position[0]))
                        Running = False
                        return

def part_2(cars, maze):
    while True:
        for car in sorted(cars, key=itemgetter("row", "col")):
            if car not in cars:
                continue
            y = car["row"]
            x = car["col"]
            current_spot = maze[y][x]
            prev_turn = car["prev_turn"]

            # Process turns (if applicable)
            if current_spot == "+":
                if car["prev_turn"] == "right":
                    car["direction"] = turn_left(car["direction"])
                    car["prev_turn"] = "left"
                elif car["prev_turn"] == "left":
                    car["prev_turn"] = "straight"
                elif car["prev_turn"] == "straight":
                    car["prev_turn"] = "right"
                    car["direction"] = turn_right(car["direction"])

            elif current_spot == "/":
                if car["direction"] == "right": car["direction"] = "up"
                elif car["direction"] == "down": car["direction"] = "left"
                elif car["direction"] == "left": car["direction"] = "down"
                elif car["direction"] == "up": car["direction"] = "right"

            elif current_spot == "\\":
                if car["direction"] == "right": car["direction"] = "down"
                elif car["direction"] == "down": car["direction"] = "right"
                elif car["direction"] == "left": car["direction"] = "up"
                elif car["direction"] == "up": car["direction"] = "left"

            # Apply movements:
            if car["direction"] == "right": car["col"] += 1
            elif car["direction"] == "left": car["col"] -= 1
            elif car["direction"] == "down": car["row"] += 1
            elif car["direction"] == "up": car["row"] -= 1

            # Check collisions:
            positions = [(car["row"], car["col"]) for car in cars]
            if len(positions) != len(set(positions)):
                for position in set(positions):
                    if positions.count(position) > 1:
                        cars = list(filter(lambda car: (car["row"], car["col"]) != position, cars))

        if len(cars) == 1:
            print("Part 2: {},{}".format(cars[0]["col"], cars[0]["row"]))
            break

if __name__ == "__main__":
    filename = "day13.txt"
    cars, maze = get_input(filename)
    part_1(cars, maze)
    cars, maze = get_input(filename)
    part_2(cars, maze)

