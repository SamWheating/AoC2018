import copy

with open('day10.txt') as f:
    input = f.readlines()

points = []
for row in input:
    # Example row: 
    # position=< 20168,  40187> velocity=<-2, -4>
    x = int(row.split("<")[1][:row.split("<")[1].index(",")])
    y = int(row.split(",")[1][:row.split(",")[1].index(">")])
    dx = int(row.split("<")[2][:row.split("<")[2].index(",")])
    dy = int(row.split(",")[2][:row.split(",")[2].index(">")])
    points.append([x,y,dx,dy])

def render_points(points):
    x_width = max([point[0] for point in points]) - min([point[0] for point in points])
    y_height = max([point[1] for point in points]) - min([point[1] for point in points])
    y_min = min([point[1] for point in points])
    x_min = min([point[0] for point in points])
    canvas  = [[" " for i in range(x_width+1)] for i in range(y_height+1)]
    for point in points:
        canvas[point[1] - y_min][point[0] - x_min] = "@"
    print("\n")
    for row in canvas:
        print("".join([i for i in row]))
    print("\n")

prev_points = []
i = 0
size = 100000000000
while(True):
    # update points:
    for point in points:
        point[0] += point[2]
        point[1] += point[3]
    x_width = max([point[0] for point in points]) - min([point[0] for point in points])
    y_height = max([point[1] for point in points]) - min([point[1] for point in points])

    if x_width * y_height > size:
        print("Canvas size {}x{}".format(x_width, y_height))
        render_points(prev_points)
        print("Took {} seconds.".format(i))
        break

    else:
        size = x_width * y_height
        prev_points = copy.deepcopy(points)
        i += 1
    
