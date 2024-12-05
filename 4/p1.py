input = open("input.txt", "r").readlines()

input = [list(x) for x in input]
for row in input:
    for char in row:
        if char == "\n":
            row.remove(char)

count_xmas = 0
for row_number, row in enumerate(input):
    for col_number, char in enumerate(row):
        if char == "X":
            # UP
            if row_number - 3 >= 0:
                up = (
                    char
                    + input[row_number - 1][col_number]
                    + input[row_number - 2][col_number]
                    + input[row_number - 3][col_number]
                )
                if up == "XMAS":
                    count_xmas += 1
            # DOWN
            if row_number + 3 < len(input):
                down = (
                    char
                    + input[row_number + 1][col_number]
                    + input[row_number + 2][col_number]
                    + input[row_number + 3][col_number]
                )
                if down == "XMAS":
                    count_xmas += 1
            # LEFT
            if col_number - 3 >= 0:
                left = (
                    char
                    + row[col_number - 1]
                    + row[col_number - 2]
                    + row[col_number - 3]
                )
                if left == "XMAS":
                    count_xmas += 1
            # RIGHT
            if col_number + 3 < len(row):
                right = (
                    char
                    + row[col_number + 1]
                    + row[col_number + 2]
                    + row[col_number + 3]
                )
                if right == "XMAS":
                    count_xmas += 1

            # DIAGONAL
            # UP-LEFT
            if row_number - 3 >= 0 and col_number - 3 >= 0:
                up_left = (
                    char
                    + input[row_number - 1][col_number - 1]
                    + input[row_number - 2][col_number - 2]
                    + input[row_number - 3][col_number - 3]
                )
                if up_left == "XMAS":
                    count_xmas += 1
            # UP-RIGHT
            if row_number - 3 >= 0 and col_number + 3 < len(row):
                up_right = (
                    char
                    + input[row_number - 1][col_number + 1]
                    + input[row_number - 2][col_number + 2]
                    + input[row_number - 3][col_number + 3]
                )
                if up_right == "XMAS":
                    count_xmas += 1
            # DOWN-LEFT
            if row_number + 3 < len(input) and col_number - 3 >= 0:
                down_left = (
                    char
                    + input[row_number + 1][col_number - 1]
                    + input[row_number + 2][col_number - 2]
                    + input[row_number + 3][col_number - 3]
                )
                if down_left == "XMAS":
                    count_xmas += 1
            # DOWN-RIGHT
            if row_number + 3 < len(input) and col_number + 3 < len(row):
                down_right = (
                    char
                    + input[row_number + 1][col_number + 1]
                    + input[row_number + 2][col_number + 2]
                    + input[row_number + 3][col_number + 3]
                )
                if down_right == "XMAS":
                    count_xmas += 1

print(count_xmas)

# """
# Up:
#     Row: 3 - 9
#     Col: 0 - 9
#
# Down:
#     Row: 0 - 6
#     Col: 0 - 9
#
# Left:
#     Row: 3 - 9
#     Col: 0 - 9
#
# Right:
#     Row: 6 - 9
#     Col: 0 - 9
#
# Diagonal:
#     Up:
#         Left:
#             Row: 3 - 9
#             Col: 3 - 9
#         Right:
#             Row: 0 - 6
#             Col: 3 - 9
#
#     Down:
#         Left:
#             Row: 3 - 9
#             Col: 0 - 6
#         Right:
#             Row: 0 - 6
#             Col: 0 - 6
#
#
# """
