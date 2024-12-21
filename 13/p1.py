import math
import time

puzzle = open("example.txt", "r").readlines()

machines = []
machine = []
for line in puzzle:
    if line != "\n":
        line = line.replace("\n", "")
        split_line = line.split(": ")
        split_xy = split_line[1].split(", ")
        if split_line[0] != "Prize":
            split_button = split_line[0].split(" ")
            button = split_button[1]
            x = split_xy[0].split("+")[1]
            y = split_xy[1].split("+")[1]
            button = [int(x), int(y)]
        else:
            x = split_xy[0].split("=")[1]
            y = split_xy[1].split("=")[1]
            button = [int(x), int(y)]

        machine.append(button)

        if len(machine) == 3:
            machines.append(machine)
            machine = []


for machine in machines:
    a = machine[0]
    b = machine[1]
    prize = machine[2]

    ax = a[0]
    ay = a[1]

    bx = b[0]
    by = b[1]

    prize_x = prize[0]
    prize_y = prize[1]
