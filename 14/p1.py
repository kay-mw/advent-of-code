puzzle = open("input.txt", "r").readlines()

robots = []
for line in puzzle:
    line = line.replace("\n", "")
    lines = line.split(" ")
    pos = lines[0].split("=")[1]
    vel = lines[1].split("=")[1]
    pos = list(eval(pos))
    vel = list(eval(vel))
    robots.append([pos, vel])

width = max([robot[0][0] for robot in robots]) + 1
height = max([robot[0][1] for robot in robots]) + 1

final_positions = []
for robot in robots:
    pos_x = robot[0][0]
    pos_y = robot[0][1]
    vel_x = robot[1][0]
    vel_y = robot[1][1]

    for _ in range(100):
        pos_x += vel_x
        pos_y += vel_y
        if pos_x >= width:
            pos_x = pos_x - width
        if pos_x < 0:
            pos_x = width + pos_x

        if pos_y >= height:
            pos_y = pos_y - height
        if pos_y < 0:
            pos_y = height + pos_y

    final_positions.append([pos_x, pos_y])


q1 = 0
q2 = 0
q3 = 0
q4 = 0
x_middle = (width - 1) // 2
y_middle = (height - 1) // 2
for x, y in final_positions:
    if 0 <= x < x_middle and 0 <= y < y_middle:
        q1 += 1
    if 0 <= x < x_middle and y_middle < y < height:
        q2 += 1
    if x_middle < x < width and 0 <= y < y_middle:
        q3 += 1
    if x_middle < x < width and y_middle < y < height:
        q4 += 1

print(q1 * q2 * q3 * q4)
