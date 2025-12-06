import time

t0 = time.time()

puzzle_input = open("input.txt", "r").read()

puzzle_input = list(map(int, puzzle_input.split()))
length = len(puzzle_input)

numbers = {}
for stone in puzzle_input:
    if stone == 0:
        if 1 in numbers:
            numbers[1] += 1
        else:
            numbers[1] = 1
    elif len(str(stone)) % 2 == 0:
        first_half, second_half = (
            int(str(stone)[: len(str(stone)) // 2]),
            int(str(stone)[len(str(stone)) // 2 :]),
        )

        if first_half in numbers:
            numbers[first_half] += 1
        else:
            numbers[first_half] = 1

        if second_half in numbers:
            numbers[second_half] += 1
        else:
            numbers[second_half] = 1
    else:
        if stone * 2024 in numbers:
            numbers[stone * 2024] += 1
        else:
            numbers[stone * 2024] = 1

for _ in range(75):
    new_numbers = {}
    for stone, occurences in numbers.items():
        if stone == 0:
            if 1 in new_numbers:
                new_numbers[1] += occurences
            else:
                new_numbers[1] = occurences
        elif len(str(stone)) % 2 == 0:
            first_half, second_half = (
                int(str(stone)[: len(str(stone)) // 2]),
                int(str(stone)[len(str(stone)) // 2 :]),
            )

            if first_half in new_numbers:
                new_numbers[first_half] += occurences
            else:
                new_numbers[first_half] = occurences

            if second_half in new_numbers:
                new_numbers[second_half] += occurences
            else:
                new_numbers[second_half] = occurences
        else:
            if stone * 2024 in new_numbers:
                new_numbers[stone * 2024] += occurences
            else:
                new_numbers[stone * 2024] = occurences

    total_occurences = 0
    for _, occurences in numbers.items():
        total_occurences += occurences

    print(total_occurences)

    numbers = new_numbers
