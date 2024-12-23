import os
import time

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

open("tree.txt", "w").close()

for i in range(10000):
    positions = []
    for _ in range(height):
        positions.append([" "] * width)

    for robot in robots:
        pos_x = robot[0][0]
        pos_y = robot[0][1]
        vel_x = robot[1][0]
        vel_y = robot[1][1]

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

        robot[0][0] = pos_x
        robot[0][1] = pos_y
        positions[pos_y][pos_x] = 0

    tree = ""
    for position in positions:
        for j, char in enumerate(position):
            if j == width - 1:
                tree += str(char) + "\n"
            else:
                tree += str(char)
            # tree += str(char)

    with open("tree.txt", "a") as file:
        file.write(f"{i}\n{tree}\n")

    # The problem with this approach is that it doesn't store the previous position.
    # This means that the robot will just move once each time.
