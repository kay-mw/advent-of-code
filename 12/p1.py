import uuid

puzzle = open("input.txt", "r").readlines()

for i, line in enumerate(puzzle):
    puzzle[i] = puzzle[i].replace("\n", "")
    puzzle[i] = list(puzzle[i])


def recursive_search(
    plot: str,
    first_time: bool,
    initial_position: list[int],
    positions: list[list[int]],
    row_length: int,
    col_length: int,
    checked_positions: list[list[int]],
    perimeter: int,
):
    new_positions = []

    for row_num, col_num in positions:
        # UP
        if row_num > 0:
            if [row_num - 1, col_num] not in checked_positions:
                up = puzzle[row_num - 1][col_num]
                if up != plot:
                    perimeter += 1
                else:
                    new_positions.append([row_num - 1, col_num])
                    checked_positions.append([row_num - 1, col_num])
        else:
            perimeter += 1

        # DOWN
        if row_num < row_length - 1:
            if [row_num + 1, col_num] not in checked_positions:
                down = puzzle[row_num + 1][col_num]
                if down != plot:
                    perimeter += 1
                else:
                    new_positions.append([row_num + 1, col_num])
                    checked_positions.append([row_num + 1, col_num])
        else:
            perimeter += 1

        # LEFT
        if col_num > 0:
            if [row_num, col_num - 1] not in checked_positions:
                left = puzzle[row_num][col_num - 1]
                if left != plot:
                    perimeter += 1
                else:
                    new_positions.append([row_num, col_num - 1])
                    checked_positions.append([row_num, col_num - 1])
        else:
            perimeter += 1

        # RIGHT
        if col_num < col_length - 1:
            if [row_num, col_num + 1] not in checked_positions:
                right = puzzle[row_num][col_num + 1]
                if right != plot:
                    perimeter += 1
                else:
                    new_positions.append([row_num, col_num + 1])
                    checked_positions.append([row_num, col_num + 1])
        else:
            perimeter += 1

    if first_time:
        checked_positions.append(initial_position)

    if new_positions:
        return recursive_search(
            plot=plot,
            first_time=False,
            initial_position=[],
            positions=new_positions,
            row_length=row_length,
            col_length=col_length,
            checked_positions=checked_positions,
            perimeter=perimeter,
        )
    else:
        return checked_positions, perimeter


visited = []
regions = {}
for row_num, row in enumerate(puzzle):
    print(row_num)
    for col_num, plot in enumerate(row):
        if row_num == 0 and col_num == 0:
            positions, perimeter = recursive_search(
                plot=plot,
                first_time=True,
                initial_position=[row_num, col_num],
                positions=[[row_num, col_num]],
                row_length=len(puzzle),
                col_length=len(row),
                checked_positions=[],
                perimeter=0,
            )
            [visited.append(position) for position in positions]
            regions[uuid.uuid4()] = {"positions": positions, "perimeter": perimeter}
        else:
            if [row_num, col_num] not in visited:
                positions, perimeter = recursive_search(
                    plot=plot,
                    first_time=True,
                    initial_position=[row_num, col_num],
                    positions=[[row_num, col_num]],
                    row_length=len(puzzle),
                    col_length=len(row),
                    checked_positions=[],
                    perimeter=0,
                )
                [visited.append(position) for position in positions]
                regions[uuid.uuid4()] = {"positions": positions, "perimeter": perimeter}

price = 0
for region in regions.values():
    area = len(region["positions"])
    perimeter = region["perimeter"]
    price += area * perimeter

print(price)
