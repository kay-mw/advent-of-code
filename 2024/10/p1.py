input = open("input.txt", "r").readlines()

parsed = []
for line in input:
    line = line.replace("\n", "")
    parsed.append(list(map(int, line)))


def recursive_trail(
    positions: list[list[int]], row_length: int, col_length: int, target: int
):
    left, right, down, up = False, False, False, False
    new_positions = []

    for row_num, col_num in positions:
        if col_num + 1 < row_length:
            left = parsed[row_num][col_num + 1]
            if left == target:
                new_positions.append([row_num, col_num + 1])
        if col_num - 1 >= 0:
            right = parsed[row_num][col_num - 1]
            if right == target:
                new_positions.append([row_num, col_num - 1])
        if row_num + 1 < col_length:
            down = parsed[row_num + 1][col_num]
            if down == target:
                new_positions.append([row_num + 1, col_num])
        if row_num - 1 >= 0:
            up = parsed[row_num - 1][col_num]
            if up == target:
                new_positions.append([row_num - 1, col_num])

    unique_positions = [list(x) for x in set(tuple(x) for x in new_positions)]

    if not new_positions:
        return False
    else:
        target += 1
        if target == 10:
            return [True] * len(unique_positions)
        else:
            return recursive_trail(
                positions=unique_positions,
                row_length=row_length,
                col_length=col_length,
                target=target,
            )


trailheads = 0
for row_num, row in enumerate(parsed):
    for col_num, num in enumerate(row):
        if num == 0:
            target = 1
            left, right, down, up = None, None, None, None
            positions = [[row_num, col_num]]
            row_length = len(parsed)
            col_length = len(row)

            ans = recursive_trail(
                positions=positions,
                row_length=row_length,
                col_length=col_length,
                target=target,
            )

            if ans:
                for _ in range(len(ans)):
                    trailheads += 1
            else:
                continue

print(trailheads)
