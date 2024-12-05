input = open("input.txt", "r").readlines()

input = [list(x) for x in input]
for row in input:
    for char in row:
        if char == "\n":
            row.remove(char)

count_xmas = 0
for row_number, row in enumerate(input):
    for col_number, char in enumerate(row):
        if char == "M" or char == "S":
            # DOWN-RIGHT
            if row_number + 2 < len(input) and col_number + 2 < len(row):
                down_right = (
                    char
                    + input[row_number + 1][col_number + 1]
                    + input[row_number + 2][col_number + 2]
                )
                if down_right == "MAS" or down_right == "SAM":
                    cross_char = input[row_number][col_number + 2]
                    if cross_char == "M" or cross_char == "S":
                        down_left_cross = (
                            cross_char
                            + input[row_number + 1][col_number + 1]
                            + input[row_number + 2][col_number]
                        )
                        if down_left_cross == "MAS" or down_left_cross == "SAM":
                            count_xmas += 1

print(count_xmas)

# There are four combinations:

# MAS
# MAS

# SAM
# SAM

# MAS
# SAM

# SAM
# MAS


# Couldn't you just check for down+right and down+left.
# Then, if it's down+right, you check two columns over for a down+left?
# If it's down+left, you check two columns over for a down+right?

# 1911 - TOO LOW
# 2698 - TOO HIGH
