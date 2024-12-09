import copy

input = open("input.txt", "r").readlines()

for i in range(len(input)):
    input[i] = list(input[i].replace("\n", ""))

possible_obstructions = []
for row_num, row in enumerate(input):
    for col_num, char in enumerate(row):
        if char != "#" and char != "^":
            obstructed = copy.deepcopy(input)
            obstructed[row_num][col_num] = "#"
            possible_obstructions.append(obstructed)


for row_num, row in enumerate(input):
    for col_num, char in enumerate(row):
        if char == "^":
            starting_position = [row_num, col_num, "UP"]

repeat_count = 0
# This takes a while...
for obstruction_num, obstruction in enumerate(possible_obstructions):
    exited = False
    positions = []
    row_num = starting_position[0]
    col_num = starting_position[1]
    direction = starting_position[2]
    while not exited:
        position = [row_num, col_num, direction]
        if position in positions:
            repeat_count += 1
            exited = True
            break
        else:
            positions.append(position)
            # UP
            if direction == "UP":
                if row_num == 0:
                    exited = True
                    break
                else:
                    facing = obstruction[row_num - 1][col_num]
                    if facing == "#":
                        direction = "RIGHT"
                        continue
                    else:
                        row_num = row_num - 1
                        continue
            # DOWN
            if direction == "DOWN":
                if row_num == len(obstruction) - 1:
                    exited = True
                    break
                else:
                    facing = obstruction[row_num + 1][col_num]
                    if facing == "#":
                        direction = "LEFT"
                        continue
                    else:
                        row_num = row_num + 1
                        continue
            # LEFT
            if direction == "LEFT":
                if col_num == 0:
                    exited = True
                    break
                else:
                    facing = obstruction[row_num][col_num - 1]
                    if facing == "#":
                        direction = "UP"
                        continue
                    else:
                        col_num = col_num - 1
                        continue
            # RIGHT
            if direction == "RIGHT":
                if col_num == len(obstruction[row_num]) - 1:
                    exited = True
                    break
                else:
                    facing = obstruction[row_num][col_num + 1]
                    if facing == "#":
                        direction = "DOWN"
                        continue
                    else:
                        col_num = col_num + 1
                        continue
