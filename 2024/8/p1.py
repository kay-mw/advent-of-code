input = open("input.txt", "r").readlines()

parsed = []
for line in input:
    line = line.replace("\n", "")
    parsed.append(line)

locations = []
for row_num, row in enumerate(parsed):
    for col_num, char in enumerate(row):
        if char != ".":
            for i in range(row_num, len(parsed)):
                for j in range(len(row)):
                    if i == row_num and j <= col_num:
                        continue
                    else:
                        if parsed[i][j] == char:
                            distance = {
                                "row": i - row_num,
                                "col": j - col_num,
                            }

                            pos_new = [i + distance["row"], j + distance["col"]]

                            pos_original = [row_num - distance["row"]]
                            if abs(distance["col"]) == distance["col"]:
                                pos_original.append(col_num - distance["col"])
                            else:
                                pos_original.append(col_num + abs(distance["col"]))

                            if 0 <= pos_new[0] < len(parsed) and 0 <= pos_new[1] < len(
                                row
                            ):
                                if pos_new not in locations:
                                    locations.append(pos_new)

                            if 0 <= pos_original[0] < len(parsed) and 0 <= pos_original[
                                1
                            ] < len(row):
                                if pos_original not in locations:
                                    locations.append(pos_original)

print(len(locations))
