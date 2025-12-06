input = open("input.txt", "r").readlines()

for i in range(len(input)):
    input[i] = list(input[i].replace("\n", ""))


all_positions = []
for row_num, row in enumerate(input):
    for col_num, char in enumerate(row):
        all_positions.append([row_num, col_num])

positions = []
direction = "UP"
exited = False
while not exited:
    for row_num, row in enumerate(input):
        for col_num, char in enumerate(row):
            if char == "^":
                positions.append([row_num, col_num])

                # UP
                if direction == "UP":
                    if row_num == 0:
                        exited = True
                        break
                    else:
                        facing = input[row_num - 1][col_num]
                        if facing == "#":
                            direction = "RIGHT"
                            continue
                        else:
                            input[row_num][col_num] = "."
                            input[row_num - 1][col_num] = "^"
                            continue
                # DOWN
                if direction == "DOWN":
                    if row_num == len(input) - 1:
                        exited = True
                        break
                    else:
                        facing = input[row_num + 1][col_num]
                        if facing == "#":
                            direction = "LEFT"
                            continue
                        else:
                            input[row_num][col_num] = "."
                            input[row_num + 1][col_num] = "^"
                            continue
                # LEFT
                if direction == "LEFT":
                    if col_num == 0:
                        exited = True
                        break
                    else:
                        facing = input[row_num][col_num - 1]
                        if facing == "#":
                            direction = "UP"
                            continue
                        else:
                            input[row_num][col_num] = "."
                            input[row_num][col_num - 1] = "^"
                            continue
                # RIGHT
                if direction == "RIGHT":
                    if col_num == len(row) - 1:
                        exited = True
                        break
                    else:
                        facing = input[row_num][col_num + 1]
                        if facing == "#":
                            direction = "DOWN"
                            continue
                        else:
                            input[row_num][col_num] = "."
                            input[row_num][col_num + 1] = "^"
                            continue


unique_positions = [x for x in all_positions if x in positions]
print(len(unique_positions))
