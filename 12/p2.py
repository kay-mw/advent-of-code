import time
import uuid

puzzle = open("example.txt", "r").readlines()

for i, line in enumerate(puzzle):
    puzzle[i] = puzzle[i].replace("\n", "")
    puzzle[i] = list(puzzle[i])


def recursive_search(
    plot: str,
    positions: list[list[int]],
    row_length: int,
    col_length: int,
    checked_positions: list[list[int]],
):
    new_positions = []

    for row_num, col_num in positions:
        if [row_num, col_num] not in checked_positions:
            checked_positions.append([row_num, col_num])

        # UP
        if row_num > 0:
            if [row_num - 1, col_num] not in checked_positions:
                up = puzzle[row_num - 1][col_num]
                if up == plot:
                    new_positions.append([row_num - 1, col_num])

        # DOWN
        if row_num < row_length - 1:
            if [row_num + 1, col_num] not in checked_positions:
                down = puzzle[row_num + 1][col_num]
                if down == plot:
                    new_positions.append([row_num + 1, col_num])

        # LEFT
        if col_num > 0:
            if [row_num, col_num - 1] not in checked_positions:
                left = puzzle[row_num][col_num - 1]
                if left == plot:
                    new_positions.append([row_num, col_num - 1])

        # RIGHT
        if col_num < col_length - 1:
            if [row_num, col_num + 1] not in checked_positions:
                right = puzzle[row_num][col_num + 1]
                if right == plot:
                    new_positions.append([row_num, col_num + 1])

    if new_positions:
        return recursive_search(
            plot=plot,
            positions=new_positions,
            row_length=row_length,
            col_length=col_length,
            checked_positions=checked_positions,
        )
    else:
        return checked_positions


def side_search(
    plot: str,
    position: dict,
    row_length: int,
    col_length: int,
    checked_positions: list[list[int]],
    edge_positions: list[list[int]],
    max_positions: int,
    sides=0,
):
    new_position = {}

    row_num = list(position.keys())[0][0]
    col_num = list(position.keys())[0][1]
    direction = list(position.values())[0]

    up = False
    down = False
    left = False
    right = False

    if [row_num, col_num] not in checked_positions:
        checked_positions.append([row_num, col_num])

    # UP
    if row_num > 0:
        if [row_num - 1, col_num] not in checked_positions:
            if puzzle[row_num - 1][col_num] == plot:
                up = True

    # DOWN
    if row_num < row_length - 1:
        if [row_num + 1, col_num] not in checked_positions:
            if puzzle[row_num + 1][col_num] == plot:
                down = True

    # LEFT
    if col_num > 0:
        if [row_num, col_num - 1] not in checked_positions:
            if puzzle[row_num][col_num - 1] == plot:
                left = True

    # RIGHT
    if col_num < col_length - 1:
        if [row_num, col_num + 1] not in checked_positions:
            if puzzle[row_num][col_num + 1] == plot:
                right = True

    if len(checked_positions) != max_positions:
        if right:
            new_position[row_num, col_num + 1] = "RIGHT"
        elif down:
            new_position[row_num + 1, col_num] = "DOWN"
        elif left:
            new_position[row_num, col_num - 1] = "LEFT"
        elif up:
            new_position[row_num - 1, col_num] = "UP"
        else:
            if direction == "UP":
                new_position[row_num + 1, col_num] = "DOWN"
            elif direction == "DOWN":
                new_position[row_num - 1, col_num] = "UP"
            elif direction == "LEFT":
                new_position[row_num, col_num + 1] = "RIGHT"
            elif direction == "RIGHT":
                new_position[row_num, col_num - 1] = "LEFT"

        print(position, new_position)
        new_direction = list(new_position.values())[0]
        if direction != new_direction:
            sides += 1

        return side_search(
            plot=plot,
            position=new_position,
            row_length=row_length,
            col_length=col_length,
            checked_positions=checked_positions,
            edge_positions=edge_positions,
            sides=sides,
            max_positions=max_positions,
        )
    else:
        return checked_positions, sides


visited = []
regions = {}
for row_num, row in enumerate(puzzle):
    for col_num, plot in enumerate(row):
        if [row_num, col_num] not in visited:
            all_positions = recursive_search(
                plot=plot,
                positions=[[row_num, col_num]],
                row_length=len(puzzle),
                col_length=len(row),
                checked_positions=[],
            )
            positions, sides = side_search(
                plot=plot,
                position={(row_num, col_num): "RIGHT"},
                row_length=len(puzzle),
                col_length=len(row),
                checked_positions=[[row_num, col_num]],
                edge_positions=[],
                max_positions=len(all_positions),
            )
            [visited.append(position) for position in positions]
            regions[f"{plot}{uuid.uuid4()}"] = {
                "positions": sorted(positions),
                "sides": sides,
            }

regions


visited = []
regions = {}
for row_num, row in enumerate(puzzle):
    for col_num, plot in enumerate(row):
        if [row_num, col_num] not in visited:
            print([row_num, col_num])
            positions, sides = side_search(
                plot=plot,
                position={(row_num, col_num): "RIGHT"},
                row_length=len(puzzle),
                col_length=len(row),
                checked_positions=[[row_num, col_num]],
                edge_positions=[],
            )
            [visited.append(position) for position in positions]
            regions[f"{plot}{uuid.uuid4()}"] = {
                "positions": sorted(positions),
                "sides": sides,
            }

regions

for id, region in regions.items():
    print(region["edges"])
    print(
        len(set([x[0] for x in region["edges"]]))
        + len(set([x[1] for x in region["edges"]]))
    )

price = 0
for region in regions.values():
    area = len(region["positions"])
    perimeter = region["perimeter"]
    price += area * perimeter

print(price)
